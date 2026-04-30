from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField
from wtforms.fields.datetime import DateTimeField
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.fields.simple import TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ViajeForm(FlaskForm):
    titulo= StringField('Titulo del Viaje', validators=[
                        DataRequired(message='El titulo es obligatorio'),
                        Length(min=3, max=100, message='El titulo debe de tener entre 3 y 100 caracteres')
        ])
    destino = StringField('Destino', validators=[
        DataRequired(message='El destino es obligatorio'),
        Length(min=3, max=100, message='El destino debe de tener entre 3 y 100 caracteres')
    ])
    descripcion = TextAreaField('Descripcion', validators=[
        DataRequired(message='La descripcion es obligatorio'),
        Length(min=10, message='La descripcion debe de tener al menos 10 caracteres')
    ])
    fecha_viaje = DateTimeField('Fecha del viaje', validators=[
        DataRequired(message='El titulo es obligatorio')
    ],format='%d/%m/%Y')

    duracion_dias = IntegerField('Duracion(dias)', validators=[
        DataRequired(message='La duracion es obligatorio'),
        NumberRange(min=1,max=365, message='La duracion debe de ser entre 1 y 365 dias')
    ])
    precio = FloatField('Precio(€)', validators=[
        DataRequired(message='El precio es obligatorio'),
        NumberRange(min=0, message='El precio debe de ser mayor o igual a 0')
    ])
    foto = FileField('Foto del viaje', validators=[
        FileRequired(message='Por favor selecciona una foto'),
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'],'Solo se permiten imagenes')
    ])
    submit = SubmitField('Guardar Viaje')
