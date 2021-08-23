from fastapi_baseplate.server.authentication import BaseAuthentication

from .env import environment


class JWTAuthHandler(BaseAuthentication):
    secret_key = environment.secret_key

    def authenticate_employee(self, token_data):
        from apps.business.models import Business
        from apps.employees.models import Employee

        sub_domain = token_data.get('business').get('sub_domain')
        employee_id = token_data.get('employee').get('id')

        business = self.session.query(Business).filter_by(sub_domain=sub_domain).one()
        employee = self.session.query(Employee).filter_by(sub_domain=sub_domain, id=employee_id).one()

        return token_data, business, employee

    def authenticate_user(self, token_data):
        pass

    def authenticate(self, token):
        token_data = super().authenticate(token)

        if token_data.get('employee') is not None:
            return self.authenticate_employee(token_data)
