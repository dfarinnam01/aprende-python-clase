import os

from flask import Flask, render_template, url_for, flash
from werkzeug.utils import redirect

from config import Config
from ejemplos.viajes_web_01.utils.utils_files import save_image, delete_image
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
    foto_nombre=""
    try:
        if form.validate_on_submit():
            foto_nombre,thumnail_nombre=save_image(form.foto.data)
            if foto_nombre:
                viaje = Viaje(titulo=form.titulo.data,
                              destino=form.destino.data,
                              descripcion=form.descripcion.data,
                              fecha_viaje=form.fecha_viaje.data,
                              duracion_dias=form.duracion_dias.data,
                              precio=form.precio.data,
                              foto_nombre=foto_nombre,
                              foto_miniatura=thumnail_nombre,)
                db.session.add(viaje)
                db.session.commit()
                flash(f'Viaje a {viaje.destino} añadido correctamente', 'success')
                return redirect(url_for('listado_viajes'))
            else:
                flash('Error al guardar la imagen. Por favor intente nuevo.', 'danger')
    except Exception as e:
        if foto_nombre:
            delete_image(foto_nombre)
        db.session.rollback()
        flash('Error al guardar el viaje. Revise los datos.', 'danger')

    return render_template('viajes/nuevo.html',form=form)

@app.route('/listado')
def listado_viajes():
    viajes =Viaje.query.order_by(Viaje.fecha_viaje).all()
    return render_template('viajes/listado.html',viajes=viajes)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)