from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import httpx
import jwt

class CustomRequest(Request):
    def __init__(self, *args, custom_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_data = custom_data


async def auth_header_middleware(request: Request, call_next):
    bearer_token = ''
    jwt_content = {}
    # Extract a specific header (e.g., 'Authorization')
    authorization_header = request.headers.get('Authorization')

    custom_data = {"extra_info": "This is extra data"}
    request.state.custom_attr = "This is my custom attribute"
    # You can perform actions with the header value here
    if authorization_header:
        if authorization_header.startswith("Bearer "):
            token = authorization_header.split("Bearer ")[1]
            jwt_content = jwt.decode(token, options={"verify_signature": False})
            request.state.jwt_content = jwt_content
            print(jwt_content)

    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        if response.status_code == 200:
            data = response.json()
            print("External API Response:", data)

            # Call the next middleware or route handler
            response1 = await call_next(request)

            return response1

              