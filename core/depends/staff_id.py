from fastapi import Request


def get_staff_id(request: Request):
    return request.state.staff_id
