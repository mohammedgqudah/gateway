from datetime import datetime

import jwt
import httpx

from fastapi import Request, HTTPException, Response
from fastapi_baseplate.server import status
from sentry_sdk import capture_message, push_scope

from core.config import SERVICES

auth_key = 'JWT'

SERVICE_UNAVAILABLE = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail='Service is currently unavailable'
)
SERVICE_TIMEOUT = SERVICE_UNAVAILABLE


class Broker:
    alias = None
    name = None

    __slots__ = ('request', 'host', 'key', 'timeout')

    def __init__(self, request):
        service_config: dict = SERVICES.get(self.alias)
        assert service_config, (
            f"Can't find configuration for service `{self.alias}`"
            f" are you sure it's in config.SERVICES['{self.alias}']"
        )
        self.request: Request = request
        self.host: str = service_config.get('host')
        self.key: str = service_config.get('key')
        self.timeout = service_config.get('timeout', 16)

    @property
    def token_payload(self):
        # TODO: different payload if you're a customer/user
        payload = {
            'employee': {
                'id': self.request.state.employee.id
            },
            'business': {
                'id': self.request.state.business.id,
                'sub_domain': self.request.state.business.sub_domain
            },
            'created_at': datetime.now().timestamp()
        }
        return payload

    def make_token(self):
        return jwt.encode(self.token_payload, key=self.key, algorithm='HS256').decode('utf-8')

    def get_auth_token(self):
        return f"{auth_key} {self.make_token()}"

    def get_headers(self, extras=None):
        extras = extras or {}

        defaults = {
            "X-Forwarded-Host": "self.request._get_raw_host()",
            "X-Forwarded-Path": self.request.url.path,
            "X-Forwarded-Scheme": self.request.url.scheme,

            "X-Request-Id": "self.get_request_tag()",
            "X-User-Agent": "self.get_user_agent()"
        }
        if hasattr(self.request.state, 'token_data'):
            defaults['Authorization'] = self.get_auth_token()

        return {**defaults, **extras}

    def make_url(self, *args):
        url = f"{self.host}/"
        for arg in args:
            url += f"{arg}/"

        return url

    def capture_exception(self, *args, **kwargs):
        with push_scope() as scope:
            scope.set_tag("broker", self.alias)
            scope.set_extra("token_payload", self.token_payload)
            if hasattr(args[0], 'request'):
                scope.set_extra("request", args[0].request)
            capture_message(*args, **kwargs, scope=scope)

    async def make_request(self, method, url, timeout=None, headers=None, **kwargs):
        timeout = timeout or self.timeout
        headers = headers or {}
        kwargs.update({
            'headers': self.get_headers(headers)
        })

        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(method=method, url=url, timeout=timeout, **kwargs)
                status_code = response.status_code
                content_type = response.headers.get("content-type", None)
                if status.is_server_error(status_code):
                    raise SERVICE_UNAVAILABLE

                return Response(
                    content=response.content,
                    status_code=status_code,
                    media_type=content_type
                )

        except httpx.TimeoutException as e:
            self.capture_exception(e)
            raise SERVICE_TIMEOUT
        except (httpx.RequestError, httpx.InvalidURL) as e:
            print(e)
            self.capture_exception(e)
            raise SERVICE_UNAVAILABLE

    def __str__(self):
        return f"<%s: %s>" % (self.name, self.host)
