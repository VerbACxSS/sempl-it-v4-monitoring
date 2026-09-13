import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import RegisterTortoise

from .middlewares.TokenValidationMiddleware import TokenValidationMiddleware

load_dotenv()

from . import router


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    config = {
        'connections': {
            'default': {
                'engine': 'tortoise.backends.mysql',
                'credentials': {
                    'host': os.getenv('MYSQL_HOST', 'localhost'),
                    'port': os.getenv('MYSQL_PORT', 20050),
                    'user': os.getenv('MYSQL_USER', 'sempl-it-user'),
                    'password': os.getenv('MYSQL_PASSWORD', 'sempl-it-password'),
                    'database': os.getenv('MYSQL_DATABASE', 'sempl-it-database'),
                }
            }
        },
        'apps': {
            'models': {
                'models': ['app.tortoise_models'],
            }
        }
    }
    async with RegisterTortoise(app=_app, config=config, generate_schemas=True, _create_db=False):
        yield


# Initialize the FastAPI application
app = FastAPI(title="VerbACxSS SEMPL-IT Monitoring API", lifespan=lifespan)

# Add middlewares (CORS and Token Validation)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(TokenValidationMiddleware)

# Include routers
app.include_router(router.router, prefix='/api/v1', tags=["api"])
