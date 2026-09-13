import os

from fastapi import HTTPException, FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED

EXCLUDED_PATHS = {"/api/v1/healthcheck", "/docs", "/openapi.json"}

class TokenValidationMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if path not in EXCLUDED_PATHS:
            token = request.headers.get("Authorization")
            if not token or not TokenValidationMiddleware.validate_token(token):
                return JSONResponse(
                    status_code=HTTP_401_UNAUTHORIZED,
                    content={"detail": "Invalid or missing token"}
                )

        response = await call_next(request)
        return response

    # Example token validation function
    @staticmethod
    def validate_token(token: str) -> bool:
        api_key = os.environ.get("MONITORING_API_KEY", "123456789")
        return token == f"Bearer {api_key}"
