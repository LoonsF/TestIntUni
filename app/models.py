from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Alumno(Base):
    __tablename__ = "alumnos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    tareas = relationship("Tarea", back_populates="alumno")

class Materia(Base):
    __tablename__ = "materias"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    tareas = relationship("Tarea", back_populates="materia")

class Tarea(Base):
    __tablename__ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(String(500))
    calificacion = Column(Float, default=0.0)
    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    materia_id = Column(Integer, ForeignKey("materias.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    alumno = relationship("Alumno", back_populates="tareas")
    materia = relationship("Materia", back_populates="tareas")