from app import crud, schemas

def test_create_materia(db_session, materia_data):
    materia = schemas.MateriaCreate(**materia_data)
    result = crud.create_materia(db_session, materia)
    assert result.nombre == materia_data["nombre"]
    assert result.codigo == materia_data["codigo"]
    assert result.id is not None

def test_get_materia(db_session, materia_data):
    materia = schemas.MateriaCreate(**materia_data)
    created = crud.create_materia(db_session, materia)
    retrieved = crud.get_materia(db_session, created.id)
    assert retrieved.id == created.id
    assert retrieved.codigo == materia_data["codigo"]

def test_get_materias(db_session, materia_data):
    materia = schemas.MateriaCreate(**materia_data)
    crud.create_materia(db_session, materia)
    materias = crud.get_materias(db_session)
    assert len(materias) == 1
    
    assert materias[0].nombre == materia_data["nombre"]
def test_update_materia(db_session, materia_data):
    materia = schemas.MateriaCreate(**materia_data)
    created = crud.create_materia(db_session, materia)
    
    update_data = schemas.MateriaUpdate(nombre="Física Updated")
    updated = crud.update_materia(db_session, created.id, update_data)
    
    assert updated.nombre == "Física Updated"
    assert updated.codigo == materia_data["codigo"]

def test_delete_materia(db_session, materia_data):
    materia = schemas.MateriaCreate(**materia_data)
    created = crud.create_materia(db_session, materia)
    
    success = crud.delete_materia(db_session, created.id)
    assert success is True
    
    deleted = crud.get_materia(db_session, created.id)
    assert deleted is None