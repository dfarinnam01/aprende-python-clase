from flask import current_app, url_for


class Filtros:

    @staticmethod
    def fecha_hora(valor):
        if valor:
            return valor.strftime('%d/%m/%Y %H:%M')
        return ''

    @staticmethod
    def euros(valor):
        return (f"{valor:,.2f} €"
                .replace(",", "X")
                .replace(".",",")
                .replace("X","."))
    def thumbnail_url(filename):
        if not filename:
            return None
        folder = current_app.config['UPLOAD_FOLDER_IMAGES_THUMBNAILS']
        return url_for('static',filename=f"{folder}/{filename}")
    @staticmethod
    def register(app):
        app.add_template_filter(Filtros.fecha_hora, 'fecha_hora')
        app.add_template_filter(Filtros.euros, 'euros')
        app.add_template_filter(Filtros.thumbnail_url, 'thumbnail_url')