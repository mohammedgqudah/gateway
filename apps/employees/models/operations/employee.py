import bcrypt
from sqlalchemy import orm
from fastapi import status, HTTPException

from apps.auth.utils import get_access_refresh_token
from ..employee import Employee

EMPLOYEE_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="An employee with this email does not exist"
)

INCORRECT_PASSWORD = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Incorrect password"
)


def get_hashed_password(raw_password: bytes) -> str:
    return bcrypt.hashpw(raw_password, bcrypt.gensalt()).decode("utf-8")


def check_password(raw_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(str.encode(raw_password), str.encode(hashed_password))


def get_employee_by_email(session: orm.Session, sub_domain, email):
    try:
        return (
            session.query(Employee.id, Employee.sub_domain, Employee.password)
            .filter_by(sub_domain=sub_domain, email=email)
            .one()
        )
    except orm.exc.NoResultFound:
        raise EMPLOYEE_NOT_FOUND


def employee_login(session: orm.Session, employee, password: str):
    authenticated = check_password(password, employee.password)
    if not authenticated:
        raise INCORRECT_PASSWORD

    payload = {
        'employee': {
            'id': employee.id
        },
        'business': {
            'sub_domain': employee.sub_domain
        }
    }
    return get_access_refresh_token(session, payload)
