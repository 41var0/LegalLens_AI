from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base

# Ayuda con las relaciones entre tablas:
# https://medium.com/@janhaviborde23/implement-one-to-many-relationship-in-fastapi-and-mysql-1179e1ad30e2

class xxxxxx(Base):
    __tablename__ = "xxxxxx"

    xxxxxx_id = Column(Integer, primary_key=True, index=True, autoincrement=True)  #se genera automáticamente
    x1: str = Column(String(100), nullable=False)
    x2: str = Column(String(100), nullable=False)
    x3 = Column(Integer, nullable=False)

    # Relationship: User has many posts
    # x_evento = relationship("Evento", back_populates="xxxxxx")


#
# class Evento(Base):
#     __tablename__ = "evento"
#
#     evento_id = Column(Integer, primary_key=True, index=True, autoincrement=True)  #se genera automáticamente
#     nombre = Column(String(100), nullable=False)
#     fecha = Column(Date, nullable=False)
#     precio = Column(Float, nullable=False)
#     tickets_vendidos = Column(Integer, nullable=False)
#
#
#     xxxxxx_id = Column(Integer, ForeignKey("xxxxxx.xxxxxx_id"), nullable=False) # Foreign key
#     # Relationship
#     xxxxxx = relationship("Xxxxxx", back_populates="evento")
#

