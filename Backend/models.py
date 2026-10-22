from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated

# Convierte ObjectId de Mongo a str automáticamente
PyObjectId = Annotated[str, BeforeValidator(lambda v: str(v) if v is not None else v)]

class Equipos(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias='_id')
    equipo: str 
    marca_specs: Optional[str] = None
    precio_venta: float = 0.0
    garantia_activa: bool = True

    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
        "json_encoders": {object: str}
    }

class UpdateEquipos(BaseModel):
    equipo: Optional[str] = None
    marca_specs: Optional[str] = None
    precio_venta: Optional[float] = None
    garantia_activa: Optional[bool] = None
    
    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
        "json_encoders": {object: str}
    }