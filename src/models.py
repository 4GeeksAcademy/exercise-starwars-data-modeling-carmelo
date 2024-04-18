import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    favoritosPersonajes = relationship('FavoritosPersonajes', backref='personajes', lazy=True)


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    diameter = Column(String(250),nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    favoritosPlanetas = relationship('FavoritosPlanetas', backref='planetas', lazy=True)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    model = Column(String(250),nullable=False)
    vehicle_class = Column(String(250),nullable=False)
    length = Column(String(250),nullable=False)
    favoritosVehiculos = relationship('FavoritosVehiculos', backref='vehiculos', lazy=True)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)
    password = Column(String(250),nullable=False)
    favoritosUsuario = relationship('FavoritosUsuario', backref='usuario', lazy=True)



class FavoritosPersonajes(Base):
    __tablename__ = 'favoritos_personajes'
    id = Column(Integer,primary_key=True)    
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
        
class FavoritosPlanetas(Base):
    __tablename__ = 'favoritos_planetas'
    id = Column(Integer,primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))

class FavoritosVehiculos(Base):
    __tablename__ = 'favoritos_vehiculos'
    id = Column(Integer,primary_key=True)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))

class FavoritosUsuario(Base):
    __tablename__ = 'favoritos_usuario'
    id = Column(Integer,primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    
    





def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
