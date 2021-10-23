from fastapi_baseplate.server.authentication import CheckAccessToken as FastAPIBasisCheckAccessToken


class CheckAccessToken(FastAPIBasisCheckAccessToken):
    def check(self, request, handler_response):
        token_data, business, employee = handler_response

        request.state.token_data = token_data
        request.state.business = business
        request.state.employee = employee
