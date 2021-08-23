from fastapi import status, Depends
from fastapi_baseplate.server.response import http_response
from fastapi_baseplate.clients.sqlalchemy.depends import get_db_session

from core.router import APIRouter
from apps.employees.models.operations.employee import get_employee_by_email, employee_login
from ..serializers import LoginData

router = APIRouter()


@router.post(
    '/login'
)
def login(credentials: LoginData, session=Depends(get_db_session())):
    """Login as a business employee."""
    employee = get_employee_by_email(
        session=session,
        sub_domain=credentials.sub_domain,
        email=credentials.email
    )
    access_token, refresh_token = employee_login(session, employee, credentials.password)

    return http_response(
        data={
            'access_token': access_token.decode('utf-8'),
            'refresh_token': refresh_token
        },
        status=status.HTTP_200_OK,
    )
