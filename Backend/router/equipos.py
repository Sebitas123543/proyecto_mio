from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import (
    get_todos_equipos,
    get_one_equipo_id,
    get_equipo_por_nombre,
    create_equipo,
    update_equipo,
    delete_equipo
)
from models import Equipos, UpdateEquipos

equipo_router = APIRouter()

@equipo_router.get('/api/equipos')
async def get_equipos():
    return await get_todos_equipos()

@equipo_router.post('/api/equipos')
async def save_equipo(item: Equipos):
    existente = await get_equipo_por_nombre(item.equipo)
    if existente:
        raise HTTPException(status_code=400, detail="El nombre del equipo ya existe")
    
    dict_item = item.model_dump()
    if dict_item.get('id') is None:
        del dict_item['id']
        
    return await create_equipo(dict_item)

@equipo_router.get('/api/equipos/{id}', response_model=Equipos)
async def get_equipo(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    res = await get_one_equipo_id(id)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@equipo_router.put('/api/equipos/{id}', response_model=Equipos)
async def put_equipo(id: str, item: UpdateEquipos):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    res = await update_equipo(id, item)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Equipo no encontrado")

@equipo_router.delete('/api/equipos/{id}')
async def remove_equipo(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID inválido")
    res = await delete_equipo(id)
    if res:
        return {"message": "Equipo eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")