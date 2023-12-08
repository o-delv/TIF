#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy 

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app
app = Flask(__name__)

# permita acceder desde el frontend al backend
CORS(app)


# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:A.L,P-123.OD@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)


# Definir la tabla 
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    precio=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    direccion=db.Column(db.String(400))

    def __init__(self,nombre,precio,cantidad,direccion):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.cantidad=cantidad
        self.direccion=direccion

# 8. Crear la tabla al ejecutarse la app
with app.app_context():
    db.create_all()

# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar pedidos de Powerful Fitness'

# Crear un registro en la tabla Productos
@app.route("/registro", methods=['POST']) 
def registro():
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    nombre_recibido = request.json["nombre"]
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    direccion=request.json['direccion']

    nuevo_registro = Pedido(nombre=nombre_recibido,precio=precio,cantidad=cantidad,direccion=direccion)
    db.session.add(nuevo_registro)
    db.session.commit()

    return "Solicitud de post recibida"
    

# Retornar todos los registros en un Json
@app.route("/pedidos",  methods=['GET'])
def pedidos():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Pedido.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "nombre":objeto.nombre, "precio":objeto.precio, "cantidad":objeto.cantidad, "direccion":objeto.direccion})

    return jsonify(data_serializada)


# Modificar un registro
@app.route('/update/<id>', methods=['PUT'])
def update(id):
    # Buscar el registro a modificar en la tabla por su id
    pedido = Pedido.query.get(id)

    # {"nombre": "Felipe"} -> input tiene el atributo name="nombre"
    nombre = request.json["nombre"]
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    direccion=request.json['direccion']

    pedido.nombre=nombre
    pedido.precio=precio
    pedido.cantidad=cantidad
    pedido.direccion=direccion
    db.session.commit()

    data_serializada = [{"id":pedido.id, "nombre":pedido.nombre, "precio":pedido.precio, "cantidad":pedido.cantidad, "direccion":pedido.direccion}]
    
    return jsonify(data_serializada)

   
@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    
    # Se busca a la pedidos por id en la DB
    pedido = Pedido.query.get(id)

    # Se elimina de la DB
    db.session.delete(pedido)
    db.session.commit()

    data_serializada = [{"id":pedido.id, "nombre":pedido.nombre, "precio":pedido.precio, "cantidad":pedido.cantidad, "direccion":pedido.direccion}]

    return jsonify(data_serializada)


if __name__ == "__main__":
    app.run(debug=True)

