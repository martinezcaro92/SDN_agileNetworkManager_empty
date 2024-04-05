# Import required libraries
from fastapi import APIRouter, HTTPException
from fastapi.testclient import TestClient
# from src.nbi.schemas import not_found, bad_request, list_of_all_types_of_topologies, TopologyComplete, tsn_topologies, metro_topologies
from api.models import NoteDB, NoteSchema, TopologyComplete, Topology, BadRequest, Deleted, TopologyList
from typing import List
# from tests.mocks.sdn_controllers import get_tsn_topology_info, get_metro_topology_info

from DatabaseHandler import DatabaseHandler
from uuid import uuid4
import json, pika, requests


# MongoDB handler for CRUD operations
db = DatabaseHandler('Define URL', 'Define DB_name', 'Define User', 'Define Password')


# Inicializar FastAPI
router = APIRouter()


# Endpoint GET /topologies
@router.get("/", description="GET description", summary="GET summary",
                  responses={200: {"model": List[TopologyComplete], "description": "Successful Response"}, 400: {"model": BadRequest, "description": "Item not found"}})
async def get_topologies():
    # Complete the method here
    delete_it = []
    
# Endpoint POST /topologies
@router.post("/", description="POST description", summary="POST summary",
                  responses={200: {"model": Topology, "description": "Successful Response"}, 400: {"model": BadRequest, "description": "Bad Request"}})
async def post_topology(topology: Topology):
    # Complete the method here
    delete_it = []

# Endpoint DELETE /topologies/
@router.delete("/", description="DELETE description", summary="DELETE summary",
                     responses={200: {"model": Deleted, "description": "Successful Response"}, 400: {"model": BadRequest, "description": "Bad Request"}})
async def delete_all_topologies():
    # Complete the method here
    delete_it = []

# Endpoint PUT /controllers/{controller_id}
@router.put("/{topology_id}", description="PUT description by id", summary="PUT summary by id",
                     responses={200: {"model": TopologyComplete, "description": "Successful Response"}, 404: {"model": BadRequest, "description": "Item not found"}})
async def put_topology_by_id(topology_id: str, topology: Topology):
    # Complete the method here
    delete_it = []