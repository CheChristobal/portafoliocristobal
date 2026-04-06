import os
from flask import Blueprint, render_template

# Definimos el Blueprint para que el orquestador lo detecte (termina en _bp)
picada_colombiana_bp = Blueprint('picada_colombiana', __name__, template_folder='templates')

@picada_colombiana_bp.route('/')
def index():
    # Datos del local extraídos de la zona de Independencia
    info_contacto = {
        "nombre_local": "Picada Colombiana",
        "direccion": "Av. Independencia 1856, Independencia, Región Metropolitana",
        "telefono": "+56 9 1234 5678",
        "comuna": "Independencia, Santiago",
        "horario": "Lunes a Domingo: 18:00 - 02:00",
        "mapa_link": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3330.224564281781!2d-70.655848!3d-33.418721!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c5e56e0d37e5%3A0x2a16d5b0b0b0b0b0!2sAv.%20Independencia%201856%2C%20Independencia%2C%20Regi%C3%B3n%20Metropolitana!5e0!3m2!1ses!2scl!4v1712345678901!5m2!1ses!2scl"
    }

    # Como el menú es una LISTA, el HTML de este proyecto NO debe usar .items()
    menu = [
        {"item": "Hamburguesa Súper Colombiana", "precio": "8.500", "tag": "Popular"},
        {"item": "Arepa Burger Especial", "precio": "7.900", "tag": "Recomendado"},
        {"item": "Sándwich Colombiano Premium", "precio": "6.500", "tag": "Especial"},
        {"item": "Empanadas Vallunas (6 unidades)", "precio": "4.200", "tag": "Entrada"},
        {"item": "Perro Caliente Callejero", "precio": "5.500", "tag": "Clásico"},
        {"item": "Arepa con Todo", "precio": "6.800", "tag": "Tradicional"}
    ]
    
    testimonios = [
        {"nombre": "Pablo Evia", "comentario": "Excelente referencia para unas hamburguesas, además que ofrecen empanadas y arepas únicas.", "rol": "Local Guide"},
        {"nombre": "Sergio Andrés", "comentario": "Una picada increíble cerca del trabajo. Atienden muy bien y preparan sándwiches deliciosos.", "rol": "Cliente Frecuente"},
        {"nombre": "brayan andres pelaez", "comentario": "El mejor sitio colombiano en Independencia, Santiago de Chile.", "rol": "Local Guide"}
    ]
    
    # IMPORTANTE: Renderizamos hacia la subcarpeta específica
    return render_template('LosCafeteros/index.html', menu=menu, testimonios=testimonios, contacto=info_contacto)