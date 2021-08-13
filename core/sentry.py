import sentry_sdk

from core.env import environment


def init(*args, **kwargs):
    kwargs.setdefault('dsn', environment.sentry_dsn)
    kwargs.setdefault('environment', environment.api_env)

    return sentry_sdk.init(*args, **kwargs)
