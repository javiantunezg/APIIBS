from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.token import verify_token, refresh_access_token

class TokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        print ('entro en middleware')
        print(token)
        if token:
            print('hay token')
            token = token.split(" ")[1]  # Remove 'Bearer ' prefix
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            try:
                # Verificar si el token de acceso es válido
                verify_token(token, credentials_exception)
            except HTTPException as e:
                if e.status_code == status.HTTP_401_UNAUTHORIZED:
                    # Intentar renovar el token de acceso
                    refresh_token = request.headers.get("X-Refresh-Token")
                    if refresh_token:
                        try:
                            new_access_token = refresh_access_token(refresh_token)
                            response = await call_next(request)
                            response.headers["Authorization"] = f"Bearer {new_access_token}"
                            return response
                        except HTTPException as refresh_exception:
                            return JSONResponse(status_code=refresh_exception.status_code, content=refresh_exception.detail)
                    else:
                        return JSONResponse(status_code=e.status_code, content=e.detail)
        print('no hay token')
        return await call_next(request)
