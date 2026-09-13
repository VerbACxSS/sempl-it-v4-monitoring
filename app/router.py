from fastapi import APIRouter

from .routers import healthcheck_router
from .routers import monitor_router

router = APIRouter()

router.include_router(healthcheck_router.router, prefix='/healthcheck', tags=['health-check'])
router.include_router(monitor_router.router, prefix='/monitoring', tags=['save'])
