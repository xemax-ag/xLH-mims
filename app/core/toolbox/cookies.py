from fastapi import Request
from fastapi.responses import Response


def set_cookie(key: str, value: str, expires: int, request: Request, response: Response, forced=False):
    if (request.cookies.get(key) is None) or forced:
        response.set_cookie(key=key, value=value, expires=expires)