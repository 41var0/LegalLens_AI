from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# 1. Obtener la URL de la base de datos desde una variable de entorno
# En Render, ellos te dan esta URL.
# En local, puedes poner una por defecto o usar un archivo .env
uri = environ.get('DATABASE_URI')

# FIX: SQLAlchemy requiere "postgresql://" en lugar de "postgres://"
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


# 2. Configuración del Engine
# Nota: Eliminamos 'connect_args' porque era específico para SQLite
engine = create_engine(uri)

# 3. Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clase Base para los modelos
class Base(DeclarativeBase):
    pass

# 5. Dependencia para inyectar la sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()