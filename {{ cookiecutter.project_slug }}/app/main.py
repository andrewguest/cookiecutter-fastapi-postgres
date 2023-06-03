import secure
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.healthcheck import router as healthcheck_router
from routes.songs import router as song_router


app = FastAPI(
    title="{{ cookiecutter.fastapi_title }}",
    description="{{ cookiecutter.fastapi_description }}",
    version="{{ cookiecutter.fastapi_version }}",
)
secure_headers = secure.Secure()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


# Include routers from the `routes/` folder
app.include_router(song_router)
app.include_router(healthcheck_router)


# Allow for VSCode debugging
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
