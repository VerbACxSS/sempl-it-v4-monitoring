import uvicorn

from .app import app

uvicorn.run(app, host="0.0.0.0", port=30050, log_level="info")
