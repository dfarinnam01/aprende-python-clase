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

if __name__ == "__main__":
    app.run(debug=True)
