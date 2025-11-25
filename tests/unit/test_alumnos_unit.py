from app import crud, schemas

def test_create_alumno(db_session, alumno_data):
    alumno = schemas.AlumnoCreate(**alumno_data)
    result = crud.create_alumno(db_session, alumno)
    assert result.nombre == alumno_data["nombre"]
    assert result.email == alumno_data["email"]
    assert result.id is not None

def test_get_alumno(db_session, alumno_data):
    alumno = schemas.AlumnoCreate(**alumno_data)
    created = crud.create_alumno(db_session, alumno)
    retrieved = crud.get_alumno(db_session, created.id)
    assert retrieved.id == created.id
    assert retrieved.nombre == alumno_data["nombre"]

def test_get_alumnos(db_session, alumno_data):
    alumno = schemas.AlumnoCreate(**alumno_data)
    crud.create_alumno(db_session, alumno)
    alumnos = crud.get_alumnos(db_session)
    assert len(alumnos) == 1
    assert alumnos[0].nombre == alumno_data["nombre"]