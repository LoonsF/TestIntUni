from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AlumnoBase(BaseModel):
    nombre: str
    email: str

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class MateriaBase(BaseModel):
    nombre: str
    codigo: str

class MateriaCreate(MateriaBase):
    pass

class Materia(MateriaBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    calificacion: float = 0.0
    alumno_id: int
    materia_id: int

class TareaCreate(TareaBase):
    pass

class Tarea(TareaBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True