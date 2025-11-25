from app import crud, schemas

def test_create_tarea(db_session, tarea_data):
    tarea = schemas.TareaCreate(**tarea_data)
    result = crud.create_tarea(db_session, tarea)
    assert result.titulo == tarea_data["titulo"]
    assert result.alumno_id == tarea_data["alumno_id"]
    assert result.id is not None

def test_get_tarea(db_session, tarea_data):
    tarea = schemas.TareaCreate(**tarea_data)
    created = crud.create_tarea(db_session, tarea)
    retrieved = crud.get_tarea(db_session, created.id)
    assert retrieved.id == created.id
    assert retrieved.descripcion == tarea_data["descripcion"]

def test_update_tarea_calificacion(db_session, tarea_data):
    tarea = schemas.TareaCreate(**tarea_data)
    created = crud.create_tarea(db_session, tarea)
    updated = crud.update_tarea_calificacion(db_session, created.id, 9.5)
    assert updated.calificacion == 9.5
    
def test_update_alumno_integration(client, alumno_data):
    create_response = client.post("/alumnos/", json=alumno_data)
    alumno_id = create_response.json()["id"]
    
    update_data = {"nombre": "Carlos Actualizado"}
    response = client.put(f"/alumnos/{alumno_id}", json=update_data)
    
    assert response.status_code == 200
    assert response.json()["nombre"] == "Carlos Actualizado"
    assert response.json()["email"] == alumno_data["email"]

def test_delete_alumno_integration(client, alumno_data):
    create_response = client.post("/alumnos/", json=alumno_data)
    alumno_id = create_response.json()["id"]
    
    response = client.delete(f"/alumnos/{alumno_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Alumno eliminado correctamente"
    
    get_response = client.get(f"/alumnos/{alumno_id}")
    assert get_response.status_code == 404