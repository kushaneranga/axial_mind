from fastapi import FastAPI
from axial_mind.app.api.api_v1.endpoints import services

app = FastAPI()


app.include_router(services.router)
