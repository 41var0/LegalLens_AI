from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud
import pymupdf
# from asyncio import create_task # for background tasks
# from schemas import


__author__    = "Alvaro Cordero Fernandez"
__copyright__ = "Copyleft"


# Creamos la instancia de FastAPI
app = FastAPI(
    root_path="/api",
    title="AI Engine",
    version="0.1.6",
    description="This panel execute easy-way the API methods"
)

# Crear las tablas automáticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    # Una respuesta sencilla para saber que funciona el servicio
    return {"answer": {"200" : "OK"}}


@app.post("/upload")
async def upload_pdf(archivo: UploadFile = File(...)):
    content = await archivo.read() # Esperamos a leer el archivo entero

    pdf = pymupdf.open(stream=content, filetype="PDF")
    text = ""

    # Recuperamos cada texto (y lo sumamos a lo ya existente)
    for page in pdf:
        text += page.get_text()

    return {"text": text}