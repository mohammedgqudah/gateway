from fastapi import Request


def get_business(request: Request):
    return request.state.business
