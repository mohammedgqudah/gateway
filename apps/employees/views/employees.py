from fastapi import status, Depends
from fastapi_baseplate.server.response import http_response
from fastapi_baseplate.clients.sqlalchemy.depends import with_session
from fastapi_baseplate.server.views import ListView
from fastapi_baseplate.serializers import UUID4
from sqlalchemy.orm import Session

from core.router import APIRouter
from core.depends import get_business

from ..models import Employee
from ..serializers import EmployeeOut, EmployeeQuery

router = APIRouter()


@router.get("/")
def list_employees(query: EmployeeQuery = Depends(), business=Depends(get_business), session=Depends(with_session)):
    employees = session.query(Employee).filter_by(sub_domain=business.sub_domain)

    return ListView(employees, EmployeeOut)(query)


@router.get("/{employee_id}")
def get_employee(employee_id: UUID4, business=Depends(get_business), session: Session = Depends(with_session)):
    employee = session.query(Employee).filter_by(sub_domain=business.sub_domain, id=employee_id).one()

    return http_response(data=EmployeeOut.from_orm(employee), status=status.HTTP_200_OK)
