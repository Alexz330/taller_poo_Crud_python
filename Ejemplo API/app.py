from flask import Flask, request

app= Flask(__name__)

mascotas=['perro', 'gato','conejo','loro']
alumnos=[
    {"nombre": "Juan", "carnet":"123"},
    {"nombre": "Pedro", "carnet":"555"}
]

@app.route('/', methods=['GET'])
def obtener_productos():
    return "<h1>hola mundo</h1>"

@app.route("/mostrarMascotas",methods=['GET'])
def mostrar_macotas():
    
    return mascotas

@app.route("/mostrarAlumnos",methods=['GET'])
def mostrar_alumnos():
    return alumnos

@app.route("/agregarMascota",methods=['POST'])
def agregarMascota():
    mascota=request.json['mascota']
    print(mascota)
    mascotas.append(mascota)
    return "mascota agregada!!"

@app.route("/agregarAlumno",methods=['POST'])
def agregarAlumno():
    alumno=request.json
    print(alumno)
    alumnos.append(alumno)
    return "alumno agregado!!"

@app.route("/modificarMascota",methods=['PUT'])
def modificarMascota():
     mascota=request.json['mascota']
     posicion=request.json['posicion']

     print(mascota, posicion)
     mascotas[posicion]=mascota
     return "mascota modfiicada"

@app.route("/modificarAlumno",methods=['PUT'])
def modificarAlumno():
    alumno=request.json
    print(alumno)
    
    for tempA in alumnos:
        print(tempA)
        if tempA["carnet"]==alumno["carnet"]:
            tempA["nombre"]=alumno["nombre"]
            print(tempA)            
    
    return "Alumno modfiicada"



if __name__ == '__main__':
    app.run(debug=True)