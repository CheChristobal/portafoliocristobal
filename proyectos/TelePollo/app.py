import os
from flask import Blueprint, render_template

# Detectamos la ubicación real de la carpeta TelePollo
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Definimos el Blueprint. 
# Importante: El nombre 'tele_pollo' es el que usará url_for('tele_pollo.index')
tele_pollo_bp = Blueprint('tele_pollo', __name__, template_folder='templates')

@tele_pollo_bp.route('/')
def index():
    # Datos de Tele Pollo
    info = {
        "nombre": "Tele Pollo",
        "eslogan": "El sabor que manda en Independencia",
        "direccion": "Independencia, Santiago de Chile",
        "metodos_pago": "Efectivo, Redelcom y Transferencia"
    }

    # menu es una LISTA (por eso fallaba si Flask cargaba el HTML de La Pizarra)
    menu = [
        {"item": "Pollo Asado Clásico", "desc": "Pollo siempre fresco, bien cocido.", "precio": "8.500"},
        {"item": "Promoción 13 Empanaditas", "desc": "Famosas empanaditas de queso.", "precio": "5.000"},
        {"item": "Papas Fritas XL", "desc": "Papas abundantes, estilo casero.", "precio": "3.500"},
        {"item": "Promo Pollo Bombero", "desc": "Pollo entero + Papas + Bebida 1.5L.", "precio": "14.900"}
    ]
    
    testimonios = [
        {"nombre": "Kamal Sara", "comentario": "Muy buen lugar, buena atención."},
        {"nombre": "Juan Valdivia", "comentario": "Bueno y barato. Pollo bien cocido."},
        {"nombre": "Bicicletas Vivaceta", "comentario": "Atienden cordialmente. Es rápido."},
        {"nombre": "Sebastian Lobos", "comentario": "Es rico. Las papas no son aceitosas."}
    ]
    
    # LA SOLUCIÓN: Apuntamos a la subcarpeta 'TelePollo/' para evitar colisiones
    return render_template('TelePollo/index.html', info=info, menu=menu, testimonios=testimonios)