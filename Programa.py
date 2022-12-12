#Importar bibliotecas

from flask import Flask
from flask_sqlalchemy import *

#Crear objeto clase Flask

app=Flask(__name__)

#Configurar el acceso a la base de datos
#URL de la base de datos

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///estudiantes.sqlite3"

#Crear la base de datos

db=SQLAlchemy(app)

#Definir tablas de la base de datos

class estudiante(db.Model):
    #Definir una llave primaria (identificador unico)
    id=db.Column("id_estudiante",db.Integer, primary_key=True)
    
    #Definir columnas de la tabla
    nombre=db.Column(db.String(50))
    codigo=db.Column(db.String(12))
    
    def __init__(self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo
        
#Definir puntos de entrada (Rutas)
@app.route("/")

def bienvenida():
    return "Hola mundo de api"


#Crear objeto de la clase estudiante

with app.app_context():
    db.create_all()
    
    #encender servidor
    app.run(debug=True)
    
    