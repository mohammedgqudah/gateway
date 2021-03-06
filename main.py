# fmt: off
import os; os.environ.setdefault("FASTAPI_BASIS_CONFIG_MODULE", "core.config")  # noqa # fmt: on

from fastapi import FastAPI
from fastapi_baseplate.server.health_check import HealthCheck

from core import sentry
from core.urls import router

sentry.init()

app = FastAPI()

app.get("/health_check")(HealthCheck())
app.include_router(router)
