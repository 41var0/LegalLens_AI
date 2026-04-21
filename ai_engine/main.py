from fastapi import FastAPI, UploadFile, File
import pymupdf
from datetime import datetime
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableSerializable
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


#======  Configuracion de la IA  ======#
modelo_ia = "gemini-2.5-flash-lite"
temperatura= 0.3      # Seriedad con la que responde
max_tokens=None     # Maxima cantidad de tokens con los que responde
timeout=None        # Tiempo de error si se tarda mucho en dar una respuesta
max_intentos = 2    # Numero de intentos hasta dar una respuesta
#======================================#

# Creamos la instancia de FastAPI
app = FastAPI(
    root_path="/api",
    title="AI Engine",
    version="0.1.6",
    description="This panel execute easy-way the API methods"
)

# No necesitamos crear tablas ni nada

@app.get("/")
async def root():
    # Una respuesta sencilla para saber que funciona el servicio
    return {"answer": {"200" : "OK"}}



@app.post("/upload")
async def upload_pdf(archivo: UploadFile = File(...)):
    content = await archivo.read() # Esperamos a leer el archivo entero

    texto = extraer_texto(content=content)

    clausulas_abusivas, riesgo_del_docuemnto = analisis_ia(texto)

    respuesta = {
        "extracted_text":  texto,
        "red_flags": clausulas_abusivas,
        "risk_level": riesgo_del_docuemnto
    }

    return respuesta



def extraer_texto(content: bytes):
    """Extrae el texto del PDF"""
    pdf = pymupdf.open(stream=content, filetype="PDF")
    text = ""

    # Recuperamos cada texto (y lo sumamos a lo ya existente)
    for page in pdf:
        text += page.get_text()

    return text



def analisis_ia(texto:str):
    """La IA analiza el texto entregado cualitativamente"""

    print(f"{"Iniciando IA":40} | ({datetime.now()})")
    cadena_redflag, cadena_valorador_reisgo = iniciar_ia()

    print(f"{"Valorando clausulas abusivas":40} | ({datetime.now()})")
    respuesta_redflags = cadena_redflag.invoke({"content": texto})
    print(respuesta_redflags.content)
    if (not respuesta_redflags.content.isspace()):  # [VER] : gemini-2.5-flash-lite
    # if (not respuesta_redflags.content[0]["text"].isspace()): # [VER] : gemini-flash-latest
        print(respuesta_redflags.content)
        clausulas_abusivas = respuesta_redflags.content.split(",")
    else:
        clausulas_abusivas = []

    print(f"{"Valorando riesgo legal del docuemnto":40} | ({datetime.now()})")
    respuesta_valorador_reisgo = cadena_valorador_reisgo.invoke({"content": texto})
    riesgo_del_docuemnto = respuesta_valorador_reisgo.content     # [VER] : gemini-2.5-flash-lite
    # riesgo_del_docuemnto = respuesta_valorador_reisgo.content[0]["text"]    # [VER] : gemini-flash-latest
    # riesgo_del_docuemnto = None

    return clausulas_abusivas, riesgo_del_docuemnto




def iniciar_ia() -> tuple[RunnableSerializable[dict, AIMessage], RunnableSerializable[dict, AIMessage]]:
    """Inicia dos 'chain' del modelo LLM. Uno para valorar las 'redflags' y otro para valorar que tan malo es el docuemnto"""
    # 2. Inicializar el LLM
    llm = ChatGoogleGenerativeAI(
        model=modelo_ia,
        temperature=temperatura,
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_intentos,
        verbose=False
    )

    # 3. Definir la "Personalidad" y la "Tarea" (Prompt Engineering)
    # En ingles entiende bien
    system_msg = (
        "You are an assistant attorney specializing in Spanish contract law, capable of "
        "identifying even the most subtle errors in legal documents. Your task is to "
        "analyze and identify clauses that are unfair, illegal, or pose a high legal risk"
        ". You must base your analysis on general principles of Spanish law. Do not offer"
        " your personal opinion. Be precise and organized. Must respond  in Spanish."
    )

    # Dos msg humanos para encontrar dos cosas distintas
    # Este se centra en encontrar las clausulas
    human_msg_redflags = (
        "Search for unfair, illegal, or high-risk legal clauses in the following "
        "document: {content}. Return a comma-separated list of all the names of clauses "
        "of this type that you find, and nothing else; respond in Spanish. If you don’t "
        "find anything unusual, reply with a single space character, and nothing else."
    )
    # Este se centra en valorar el docuento
    human_msg_valorador_riesgo = (
        "Search for unfair, illegal, or high-risk legal clauses in the following "
        "document: {content}. You must return JUST ONE of these four options (none, low, "
        "medium, high) depending on whether the clauses you find are dangerous (high) "
        "or, conversely, normal and pose no risk (none). Do not response anything more."
    )

    prompt_redflags = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", human_msg_redflags)
    ])
    prompt_valorador_riesgo = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", human_msg_valorador_riesgo)
    ])

    # 4. Creamos dos cadenas, una para redflags y otra para valorar el riesgo legal
    chain_redflags = prompt_redflags | llm
    chain_valorador_riesgo = prompt_valorador_riesgo | llm

    return chain_redflags, chain_valorador_riesgo

