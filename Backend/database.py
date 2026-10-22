from motor.motor_asyncio import AsyncIOMotorClient
from models import Equipos, UpdateEquipos
from bson import ObjectId

cliente = AsyncIOMotorClient('mongodb://localhost')
database = cliente.tecnologiadatabase
coleccion = database.equipos

async def get_one_equipo_id(id: str):
    equipo = await coleccion.find_one({'_id': ObjectId(id)})
    if equipo:
        equipo['_id'] = str(equipo['_id'])
    return equipo

async def create_equipo(equipo_data):
    new_equipo = await coleccion.insert_one(equipo_data)
    created_equipo = await coleccion.find_one({'_id': new_equipo.inserted_id})
    if created_equipo:
        created_equipo['_id'] = str(created_equipo['_id'])
    return created_equipo

async def get_todos_equipos():
    equipos = []
    cursor = coleccion.find({})
    async for document in cursor:
        document['_id'] = str(document['_id'])
        equipos.append(Equipos(**document))
    return equipos

async def update_equipo(id: str, data: UpdateEquipos):
    equipos = data.model_dump(by_alias=True, exclude_unset=True)
    equipos.pop('id', None)
    await coleccion.update_one({'_id': ObjectId(id)}, {'$set': equipos})
    document = await coleccion.find_one({'_id': ObjectId(id)})
    if document: 
        document['_id'] = str(document['_id'])
    return document

async def delete_equipo(id: str):
    await coleccion.delete_one({'_id': ObjectId(id)})
    return True

async def get_equipo_por_nombre(equipo_nombre: str):
    item = await coleccion.find_one({'equipo': equipo_nombre})
    return item