from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ficha1/<nombre>/<apellidos>/<edad>/<localidad>")
def ficha1(nombre,apellidos,edad,localidad):
    return render_template("ficha1.html",nombre=nombre,apellidos=apellidos,edad=edad,localidad=localidad)

@app.route("/ficha2/<nombre>/<apellidos>/<edad>/<localidad>")
def ficha2(nombre,apellidos,edad,localidad):
    persona={"nombre":nombre,"apellidos":apellidos,"edad":edad,"localidad":localidad}
    return render_template("ficha1.html",**persona)

@app.route("/ficha3/<nombre>/<apellidos>/<edad>/<localidad>")
def ficha3(nombre,apellidos,edad,localidad):
    persona={"nombre":nombre,"apellidos":apellidos,"edad":edad,"localidad":localidad}
    return render_template("ficha3.html",data=persona)

@app.route('/listado1')
def listado1():
    personas=["David Fariña Morena", "Juanita Gómez Ávila", "Luisito Gonzalez Mesa"]
    return render_template("listado1.html",personas=personas)

@app.route('/listado2')
def listado2():
    empleados=[
        {"nombre":"David","apellidos":"Fariña Morena","sueldo":0},
        {"nombre": "Paco", "apellidos": "Mendoza Seramai", "sueldo": 1423},
        {"nombre": "Tomas", "apellidos": "Garrido Torro", "sueldo": 8000}
    ]
    return render_template("listado2.html",empleados=empleados)

@app.route('/listado3')
def listado3():
    empleados=[
        {"nombre":"David","apellidos":"Fariña Morena","sueldo":0},
        {"nombre": "Paco", "apellidos": "Mendoza Seramai", "sueldo": 1423},
        {"nombre": "Tomas", "apellidos": "Garrido Torro", "sueldo": 8000}
    ]
    return render_template("listado3.html",empleados=empleados)

if __name__ == "__main__":
    app.run(debug=True)
