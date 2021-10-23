from fastapi import Depends, status
from fastapi_baseplate.clients.sqlalchemy.depends import get_db_session
from fastapi_baseplate.server.response import http_response

from apps.employees.models.operations.employee import employee_login, get_employee_by_email
from core.router import APIRouter

from ..serializers import LoginCredentials

router = APIRouter()


@router.post("/login")
def login(credentials: LoginCredentials, session=Depends(get_db_session())):
    """Login as a business employee."""
    employee = get_employee_by_email(
        session=session,
        sub_domain=credentials.sub_domain,
        email=credentials.email,
    )
    access_token, refresh_token = employee_login(session, employee, credentials.password)

    return http_response(
        data={
            "access_token": access_token.decode("utf-8"),
            "refresh_token": refresh_token,
        },
        status=status.HTTP_200_OK,
    )
