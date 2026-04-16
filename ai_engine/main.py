from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud
# from schemas import


__author__    = "Alvaro Cordero Fernandez"
__copyright__ = "Copyleft"


# Creamos la instancia de FastAPI
app = FastAPI(title="EventMaster", version="0.0.6")

# Crear las tablas automáticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    # Una respuesta sencilla para saber que funciona el servicio
    return {"answer": {"200" : "OK"}}
