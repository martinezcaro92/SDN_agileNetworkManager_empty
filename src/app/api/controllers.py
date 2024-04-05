# Importar FastAPI
from fastapi import APIRouter, HTTPException
# from src.nbi.schemas import not_found, bad_request, Controller, ControllerWithID, list_of_controllers, deleted
from api.models import NoteDB, NoteSchema, Controller, ControllerWithID, BadRequest, Deleted
from DatabaseHandler import DatabaseHandler
import json
from uuid import uuid4
from typing import List




# Inicializar FastAPI
router = APIRouter()

db = DatabaseHandler('Define URL', 'Define DB_name', 'Define User', 'Define Password')

# Endpoint GET /controllers
@router.get("/", description="GET description", summary="GET summary",
                  responses={200: {"model": List[ControllerWithID], "description": "Successful Response"}, 400: {"model": BadRequest, "description": "Bad Request"}})
async def get_controllers():
    # Complete the method here
    delete_it = []

# Endpoint POST /controllers
@router.post("/", description="POST description", summary="POST summary",
                  responses={200: {"model": ControllerWithID, "description": "Successful Response"}, 400: {"model": BadRequest, "description": "Bad Request"}})
async def post_controllers(controller: Controller):
    # Complete the method here
    delete_it = []

# Endpoint PUT /controllers/{controller_id}
@router.put("/{controller_id}", description="PUT description by id", summary="PUT summary by id",
                     responses={200: {"model": ControllerWithID, "description": "Successful Response"}, 404: {"model": BadRequest, "description": "Item not found"}})
async def put_controllers_by_id(controller_id: str, controller: Controller):
    # Complete the method here
    delete_it = []

# Endpoint DELETE /controllers
@router.delete("/", description="Deletes all description", summary="Deletes all summary",
                     responses={200: {"model": Deleted, "description": "Successful Response"}, 404: {"model": BadRequest, "description": "Item not found"}})
async def delete_all_controllers():
    # Complete the method here
    delete_it = []