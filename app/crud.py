from sqlalchemy.orm import Session
from app import models, schemas

def create_alumno(db: Session, alumno: schemas.AlumnoCreate):
    db_alumno = models.Alumno(**alumno.dict())
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return db_alumno

def get_alumno(db: Session, alumno_id: int):
    return db.query(models.Alumno).filter(models.Alumno.id == alumno_id).first()

def get_alumnos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Alumno).offset(skip).limit(limit).all()

def create_materia(db: Session, materia: schemas.MateriaCreate):
    db_materia = models.Materia(**materia.dict())
    db.add(db_materia)
    db.commit()
    db.refresh(db_materia)
    return db_materia

def get_materia(db: Session, materia_id: int):
    return db.query(models.Materia).filter(models.Materia.id == materia_id).first()

def get_materias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Materia).offset(skip).limit(limit).all()

def create_tarea(db: Session, tarea: schemas.TareaCreate):
    db_tarea = models.Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def get_tarea(db: Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

def get_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarea).offset(skip).limit(limit).all()

def update_tarea_calificacion(db: Session, tarea_id: int, calificacion: float):
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()
    if db_tarea:
        db_tarea.calificacion = calificacion
        db.commit()
        db.refresh(db_tarea)
    return db_tarea