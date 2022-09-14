from fastapi import APIRouter
from config.db import conn
from model.constructors import constructors, circuits, drivers, pit_stoprs,races,results
from schema.constructors_schema import Busqueda1
from cryptography.fernet import Fernet

#modularizar o dividir las rutas 

user = APIRouter()
key= Fernet.generate_key()
f= Fernet(key)

@user.get("/constructors")
def getConstructors():
    return conn.execute(constructors.select()).fetchall()

@user.get("/circuits")
def getCircuits():
    return conn.execute(circuits.select()).fetchall()

@user.get("/drivers")
def getDrivers():
    return conn.execute(drivers.select()).fetchall()

@user.get("/pit_stoprs")
def getpit_stoprs():
    return conn.execute(pit_stoprs.select()).fetchall()    

@user.get("/races")
def getpit_stoprs():
    return conn.execute(races.select()).fetchall()   

@user.get("/results")
def getpit_stoprs():
    return conn.execute(results.select()).fetchall()   

#@user.post("/busqueda")
# def busqueda1(user: Busqueda1):
#    resultado = conn.execute()
#    return "Hello "
