from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Académico")

# Alumnos Endpoints
@app.post("/alumnos/", response_model=schemas.Alumno)
def create_alumno(alumno: schemas.AlumnoCreate, db: Session = Depends(get_db)):
    return crud.create_alumno(db=db, alumno=alumno)

@app.get("/alumnos/", response_model=List[schemas.Alumno])
def read_alumnos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_alumnos(db, skip=skip, limit=limit)

@app.get("/alumnos/{alumno_id}", response_model=schemas.Alumno)
def read_alumno(alumno_id: int, db: Session = Depends(get_db)):
    db_alumno = crud.get_alumno(db, alumno_id=alumno_id)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return db_alumno

@app.put("/alumnos/{alumno_id}", response_model=schemas.Alumno)
def update_alumno(alumno_id: int, alumno: schemas.AlumnoUpdate, db: Session = Depends(get_db)):
    db_alumno = crud.update_alumno(db, alumno_id=alumno_id, alumno=alumno)
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return db_alumno

@app.delete("/alumnos/{alumno_id}")
def delete_alumno(alumno_id: int, db: Session = Depends(get_db)):
    success = crud.delete_alumno(db, alumno_id=alumno_id)
    if not success:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {"message": "Alumno eliminado correctamente"}

# Materias Endpoints
@app.post("/materias/", response_model=schemas.Materia)
def create_materia(materia: schemas.MateriaCreate, db: Session = Depends(get_db)):
    return crud.create_materia(db=db, materia=materia)

@app.get("/materias/", response_model=List[schemas.Materia])
def read_materias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_materias(db, skip=skip, limit=limit)

@app.get("/materias/{materia_id}", response_model=schemas.Materia)
def read_materia(materia_id: int, db: Session = Depends(get_db)):
    db_materia = crud.get_materia(db, materia_id=materia_id)
    if db_materia is None:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return db_materia

@app.put("/materias/{materia_id}", response_model=schemas.Materia)
def update_materia(materia_id: int, materia: schemas.MateriaUpdate, db: Session = Depends(get_db)):
    db_materia = crud.update_materia(db, materia_id=materia_id, materia=materia)
    if db_materia is None:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return db_materia

@app.delete("/materias/{materia_id}")
def delete_materia(materia_id: int, db: Session = Depends(get_db)):
    success = crud.delete_materia(db, materia_id=materia_id)
    if not success:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return {"message": "Materia eliminada correctamente"}

# Tareas Endpoints
@app.post("/tareas/", response_model=schemas.Tarea)
def create_tarea(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    return crud.create_tarea(db=db, tarea=tarea)

@app.get("/tareas/", response_model=List[schemas.Tarea])
def read_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tareas(db, skip=skip, limit=limit)

@app.get("/tareas/{tarea_id}", response_model=schemas.Tarea)
def read_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = crud.get_tarea(db, tarea_id=tarea_id)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.put("/tareas/{tarea_id}", response_model=schemas.Tarea)
def update_tarea(tarea_id: int, tarea: schemas.TareaUpdate, db: Session = Depends(get_db)):
    db_tarea = crud.update_tarea(db, tarea_id=tarea_id, tarea=tarea)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea

@app.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int, db: Session = Depends(get_db)):
    success = crud.delete_tarea(db, tarea_id=tarea_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada correctamente"}

@app.put("/tareas/{tarea_id}/calificar")
def calificar_tarea(tarea_id: int, calificacion: float, db: Session = Depends(get_db)):
    db_tarea = crud.update_tarea_calificacion(db, tarea_id=tarea_id, calificacion=calificacion)
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_tarea