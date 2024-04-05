from fastapi import FastAPI

from api import controllers, topologies
from fastapi.openapi.models import Contact,Server

# from app.api.models import Base
# from app.D_db import engine





# Base.metadata.create_all(bind=engine)

servers = [
    {
        "url": "URL 1",
        "description": "Description 1"
    },
    {
        "url": "URL 2",
        "description": "Description 2"
    }
]

app = FastAPI(
    title="Title example - REST API NBI",
    description="Description example - REST API NBI",
    contact=Contact(name="Authors name", url="URL here", email="email here"),
    version="0.0.1",
    servers= servers
    )



# app.include_router(ping.router)
# app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(controllers.router, prefix="/controllers", tags=["Controllers"])
app.include_router(topologies.router, prefix="/topologies", tags=["Topologies"])
