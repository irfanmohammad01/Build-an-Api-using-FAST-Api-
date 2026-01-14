from fastapi import FastAPI
import models
from database import engine
from routes.user_routes import router

app = FastAPI(title="API Assignment")

models.Base.metadata.create_all(bind=engine)

app.include_router(router)

