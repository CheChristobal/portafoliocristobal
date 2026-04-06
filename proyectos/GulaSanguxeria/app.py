import os
from flask import Blueprint, render_template

# Definimos el Blueprint para el orquestador
# El nombre 'gula' será usado para url_for('gula.index')
gula_bp = Blueprint('gula', __name__, template_folder='templates')

@gula_bp.route('/')
def index():
    # Datos maestros extraídos de las reseñas reales de Google
    context = {
        "nombre_local": "El Gula Sanguixería",
        "direccion": "Av. Salomón Sack 505",
        "comuna": "Independencia, Región Metropolitana",
        "whatsapp": "+56912345678", 
        "google_maps_link": "https://www.google.com/maps/place/Gula+Sanguxeria/@-33.4179775,-70.6735076,19z/data=!4m16!1m9!3m8!1s0x9662c4325ea58b73:0xd3157872e0edc04b!2sGula+Sanguxeria!8m2!3d-33.4184473!4d-70.6725012!9m1!1b1!16s%2Fg%2F11c2jmqpsq!3m5!1s0x9662c4325ea58b73:0xd3157872e0edc04b!8m2!3d-33.4184473!4d-70.6725012!16s%2Fg%2F11c2jmqpsq?entry=ttu&g_ep=EgoyMDI2MDQwMS4wIKXMDSoASAFQAw%3D%3D",
        
        "testimonios": [
            {"nombre": "David Núñez", "texto": "Muy buen lugar para compartir. ¡Nos dieron un consomé de cortesía!", "stars": 5},
            {"nombre": "Carolina Andrea", "texto": "El pollo asado es exquisito. Las salsas de ajo y ciboulette son deliciosas.", "stars": 5},
            {"nombre": "Juan Pedreros", "texto": "El mejor lugar de comida rápida del sector. Promociones buenísimas.", "stars": 5},
            {"nombre": "Art Tazas", "texto": "Tienen opción de carne de soja para vegetarianos. Muy ricas sus salsas.", "stars": 5}
        ],

        "menu": {
            "Sanguixes & Bajones": [
                {"item": "Gringa Mechada", "detalle": "Carne mechada premium con queso fundido real.", "precio": "6.500"},
                {"item": "Italiano Clásico", "detalle": "Palta, tomate y nuestra famosa mayo casera.", "precio": "4.500"},
                {"item": "Churrasco Dinámico", "detalle": "Palta, tomate, mayo, chucrut y americana.", "precio": "5.200"}
            ],
            "Especialidades Gula": [
                {"item": "Pollo Asado Completo", "detalle": "El más esquisito del sector, bien sazonado y jugoso.", "precio": "9.990"},
                {"item": "Chorrillana XL", "detalle": "Papas fritas de lujo, carne, cebolla y huevo.", "precio": "12.900"},
                {"item": "Chorrillana Veggie", "detalle": "Carne de soya, pimentón y champiñones.", "precio": "11.500"}
            ]
        }
    }
    
    # IMPORTANTE: Renderizamos apuntando a la subcarpeta para evitar el UndefinedError
    return render_template('GulaSanguxeria/index.html', **context)