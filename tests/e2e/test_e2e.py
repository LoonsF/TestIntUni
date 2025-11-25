def test_complete_flow_e2e(client):
    alumno_response = client.post("/alumnos/", json={
        "nombre": "María García",
        "email": "maria@example.com"
    })
    assert alumno_response.status_code == 200
    alumno_id = alumno_response.json()["id"]
    
    materia_response = client.post("/materias/", json={
        "nombre": "Programación",
        "codigo": "PROG101"
    })
    assert materia_response.status_code == 200
    materia_id = materia_response.json()["id"]
    
    tarea_response = client.post("/tareas/", json={
        "titulo": "Proyecto Final",
        "descripcion": "API REST con FastAPI",
        "alumno_id": alumno_id,
        "materia_id": materia_id
    })
    assert tarea_response.status_code == 200
    tarea_id = tarea_response.json()["id"]
    
    calificar_response = client.put(f"/tareas/{tarea_id}/calificar?calificacion=9.0")
    assert calificar_response.status_code == 200
    assert calificar_response.json()["calificacion"] == 9.0
    
    alumno_check = client.get(f"/alumnos/{alumno_id}")
    materia_check = client.get(f"/materias/{materia_id}")
    tarea_check = client.get(f"/tareas/")
    
    assert alumno_check.status_code == 200
    assert materia_check.status_code == 200
    assert tarea_check.status_code == 200
    assert len(tarea_check.json()) == 1