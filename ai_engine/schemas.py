from pydantic import BaseModel, Field
# from datetime import date

### xxxxxx ####
class xxxxxxBase(BaseModel):
    nombre: str = Field(max_length=100)
    ciudad: str = Field(max_length=100)
    capacidad: int = Field(gt=0)

class xxxxxxCreate(xxxxxxBase):
    pass

class xxxxxxUpdate(xxxxxxBase):
    pass

class xxxxxxOut(xxxxxxBase):
    xxxxxx_id: int
    class Config:
        from_attributes = True  # permite convertir objetos ORM a Pydantic
