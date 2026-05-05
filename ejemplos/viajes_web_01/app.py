import os

from flask import Flask, render_template

from config import Config
from utils.utils_files import save_image
from forms import ViajeForm
from filtros import Filtros
from models import db,Viaje

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

Filtros.register(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevo',methods=['GET','POST'])
def nuevo_viaje():
    form = ViajeForm()
    if form.validate_on_submit():
        foto_nombre,thumnail_nombre=save_image(form.foto.data)
        print("OK")
        return render_template('index.html')
    return render_template('viajes/nuevo.html',form=form)

@app.route('/listado',methods=['GET','POST'])
def listado_viajes():
    return render_template('viajes/listado.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)