from starlette.middleware.base import BaseHTTPMiddleware


class CheckApiKey(BaseHTTPMiddleware):
 async def dispatch(self, request, call_next):
    print("ok")
    response = await call_next(request)

    return response