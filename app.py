# Objetivo:# Crear una API que se conecte con una BD que tengamos en Mongo
from flask import Flask, jsonify, request
from pymongo import MongoClient


app = Flask(__name__)

# API: Application Programming Interface -< Intermedarios (Cliente - API - Server)

# APIs: Cualquier cosa que se pueda programar se puede meter en una API 

# ENDPOINT: URL pertenece a una API; Realiza operaciones

# URLBASE: Raíz de una API; Dominio; A partir de aquí se construyen todos los endpoints; Tmbn es un endpoint

# EJemplo de URLBASE: https://swapi.tech/ -> URLBASE de Sw API

# EJemplo de Endpoint: https://swapi.tech/people/:id



# Decoradores son como podemos decirle a una funcion que se comporte una una manera especifica

# @nombre_decorador -     ✅ Sintaxis Correcta

# def func_name()
#   operaciones_de_func





# @decorador -     🚫 Sintaxis Incorrecta

# print() # el codigo que sea

# def func_name()
#   operaciones_de_func



@app.route('/') # La "/" significa la raíz ergo nuestro URLBASE
def holi():
  return "Otra palabra :)"


@app.route('/resta')
def resta():
  # Mdoelos Ai
  # Analisis de datos pandas
  # Cualquier cosa que se pueda programar
  print(10-5)
  print('holi')
  return jsonify({
    "status_code": 200,
    "message": "OK",
    "result": 10-5
  })

# url_route?queryparam=value
@app.route('/minus', methods=['POST'])
def minus():
  # los "args" se refieren a los queryparameters de la peticion
  value1 = request.args.get('x', type=float)
  value2 = request.args.get('y', type=float)
  print(value1)
  print(value2)
  if value1 and value2:
    return jsonify({
    "status_code": 200,
    "message": "OK",
    "result": value1 - value2
    })
  else:
    response = jsonify({
    "status_code": 400,
    "message": "Bad Request: No obtuvimos todos los queryparams, revisalos"
    })
    response.status_code = 400
    return response

# Artistas Version 1
@app.route('/artistas', methods=['GET', 'POST'])
def mongo():
  """Se va a conectar a nuestro Cluster de Mongo, va a ir a un BD y a una coleccion, 
  hará una query y regresará los datos de esa query"""
  # Creamos una conexión con Mongo
  client = MongoClient('mongodb+srv://holi:hola@cluster0.bvlpxci.mongodb.net/')
  # Apuntamos a la base de datos 'spotify'
  db = client['spotify']
  # Apuntamos a la colección 'songs'
  coll = db['songs']
  the_doors_songs = coll.find({"artists": {"$regex": "The Doors"}},{'_id':False}).limit(10)
  results_list = list(the_doors_songs)

  print('len(results_list)')
  print(len(results_list))

  return jsonify({
    "status_code": 200,
    "message": "OK",
    "results": results_list
    })


# Artistas version 2 - Final

# Recibir valores a treavés de la ruta (path)

# Ejemplos de recibir valores a través del path


# https://URLBASE        /valor1/valor2

# https://swapi.tech/api/people/123
# https://swapi.tech/api/starships/9
# https://swapi.tech/api/planets/7

@app.route('/artistas/<nombre_de_artista>', methods=['GET', 'POST'])
def artists(nombre_de_artista):
  """Se va a conectar a nuestro Cluster de Mongo, va a ir a un BD y a una coleccion, 
  hará una query y regresará los datos de esa query"""
  # Creamos una conexión con Mongo
  client = MongoClient('mongodb+srv://holi:hola@cluster0.bvlpxci.mongodb.net/')
  # Apuntamos a la base de datos 'spotify'
  db = client['spotify']
  # Apuntamos a la colección 'songs'
  coll = db['songs']
  the_doors_songs = coll.find({"artists": {"$regex": nombre_de_artista}},{'_id':False}).limit(10)
  results_list = list(the_doors_songs)

  print('len(results_list)')
  print(len(results_list))

  return jsonify({
    "status_code": 200,
    "message": "OK",
    "results": results_list
    })


# Documentacion
#Respuesta del endpoint: va a ser un JSON con canciones
#nombre de artista debe ser un texto
#numero de canciones debe ser un numero


@app.route('/artistas/<nombre_de_artista>/<numero_de_canciones>', methods=['GET', 'POST'])
def artists_number_songs(nombre_de_artista, numero_de_canciones):
  """Se va a conectar a nuestro Cluster de Mongo, va a ir a un BD y a una coleccion, 
  hará una query y regresará los datos de esa query"""
  numero = int(numero_de_canciones)
  # Creamos una conexión con Mongo
  client = MongoClient('mongodb+srv://holi:hola@cluster0.bvlpxci.mongodb.net/')
  # Apuntamos a la base de datos 'spotify'
  db = client['spotify']
  # Apuntamos a la colección 'songs'
  coll = db['songs']
  the_doors_songs = coll.find({"artists": {"$regex": nombre_de_artista}},{'_id':False}).limit(numero)
  results_list = list(the_doors_songs)
  
  print('len(results_list)')
  print(len(results_list))

  return jsonify({
    "status_code": 200,
    "message": "OK",
    "results": results_list
    })

@app.route('/artistasQuers', methods=['GET', 'POST'])
def artists_number_songs_queryparams():
  """Se va a conectar a nuestro Cluster de Mongo, va a ir a un BD y a una coleccion, 
  hará una query y regresará los datos de esa query"""
  nombre_de_artista = request.args.get('artista')
  numero = request.args.get('canciones', type=int)
  # Creamos una conexión con Mongo
  client = MongoClient('mongodb+srv://holi:hola@cluster0.bvlpxci.mongodb.net/')
  # Apuntamos a la base de datos 'spotify'
  db = client['spotify']
  # Apuntamos a la colección 'songs'
  coll = db['songs']
  the_doors_songs = coll.find({"artists": {"$regex": nombre_de_artista}},{'_id':False}).limit(numero)
  results_list = list(the_doors_songs)
  
  print('len(results_list)')
  print(len(results_list))

  return jsonify({
    "status_code": 200,
    "message": "OK",
    "results": results_list
    })





#if (validacion?) {
  #Operaciones del if
#}














# localhost: 0.0.0.0 ó 127.0.0.1
# Port: 1-10 000; 80, 3306, 3000
app.run(debug=True,host="localhost", port=5005)