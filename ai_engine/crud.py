from sqlalchemy.orm import Session
from models import xxxxxx
from schemas import xxxxxxCreate, xxxxxxUpdate



### XXXXXX ####
def get_xxxxxxs(db: Session):
    return db.query(xxxxxx).all()

def get_xxxxxx(db: Session, id_filtro: int):
    return db.query(xxxxxx).filter(xxxxxx.xxxxxx_id == id_filtro).first()



def create_xxxxxx(db: Session, datos: xxxxxxCreate):
    nuevo_xxxxxx = xxxxxx(**datos.model_dump())
    db.add(nuevo_xxxxxx)
    db.commit()
    db.refresh(nuevo_xxxxxx) # refresca para obtener el codigo asignado
    return nuevo_xxxxxx


def update_xxxxxx(db: Session, id_filtro: int, datos: xxxxxxUpdate):
    xxxxxx_updateado = get_xxxxxx(db, id_filtro)
    if (xxxxxx_updateado):
        xxxxxx_updateado.x1 = datos.x1
        xxxxxx_updateado.x2 = datos.x2
        xxxxxx_updateado.x3 = datos.x3
        db.commit()
        db.refresh(xxxxxx_updateado)  # refresca para obtener el codigo asignado
    return xxxxxx_updateado


def delete_xxxxxx(db: Session, id_filtro: int):
    xxxxxx = get_xxxxxx(db, id_filtro)
    if (xxxxxx):
        db.delete(xxxxxx)
        db.commit()
    return xxxxxx


