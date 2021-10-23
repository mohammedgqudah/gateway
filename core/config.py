from datetime import timedelta

from fastapi_baseplate.clients.sqlalchemy import BaseQuery, create_engine
from fastapi_baseplate.conf.defaults import *  # noqa
from sqlalchemy.orm import sessionmaker as _sessionmaker

from .authentication import JWTAuthHandler
from .env import environment

SECRET_KEY = environment.secret_key

HEALTH_CHECK["checks"] += [{"name": "celery", "handler": lambda: (True, "")}]  # noqa: F405

ACTIVE_APPS = ["business", "employees", "channel"]

SERVICES = {
    "customers": {
        "host": environment.customers_host,
        "key": environment.customers_key,
    },
    "catalog": {
        "host": environment.catalog_host,
        "key": environment.catalog_key,
    },
}

ACCESS_TOKEN_EXP_DELTA = timedelta(hours=environment.access_token_exp)
JWT["AUTHENTICATION_HANDLERS"] = {"JWT": JWTAuthHandler}  # noqa: F405

engine = create_engine(environment.postgres_dsn)
sessionmaker = _sessionmaker(autocommit=False, autoflush=False, bind=engine, info={}, query_cls=BaseQuery)
