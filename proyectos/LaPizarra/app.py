from flask import Blueprint, render_template

# Definimos el Blueprint. 
# Importante: El nombre 'la_pizarra' es el que usará el orquestador
la_pizarra_bp = Blueprint('la_pizarra', __name__, template_folder='templates')

@la_pizarra_bp.route('/')
def index():
    # Estructura de DICCIONARIO: permite usar {% for categoria, items in menu.items() %}
    menu = {
        "Pizzas Artesanales": [
            {"nombre": "Pepperoni Suprema", "precio": "$9.990", "desc": "Trozos grandes de pepperoni y mozzarella extra."},
            {"nombre": "Española Pizarra", "precio": "$10.500", "desc": "Chorizo español, cebolla morada y pimentón."},
            {"nombre": "Margarita Original", "precio": "$8.500", "desc": "Albahaca fresca, tomate y aceite de oliva."}
        ],
        "Empanadas y Más": [
            {"nombre": "Pino al Horno", "precio": "$2.500", "desc": "Carne picada a cuchillo, receta de la abuela."},
            {"nombre": "Queso Champiñón", "precio": "$2.200", "desc": "Mezcla de quesos con champiñones salteados."}
        ]
    }

    # Datos para la sección de "Voces del Barrio"
    reviews = [
        {"name": "Carlos Iturra", "stars": 5, "text": "La masa es increíblemente crocante, no he probado otra igual en Independencia."},
        {"name": "Marta Gómez", "stars": 5, "text": "Atención 10/10. Se nota que los dueños le ponen amor a cada preparación."},
        {"name": "Roberto L.", "stars": 5, "text": "Los trozos de los ingredientes son reales, nada de láminas delgadas."}
    ]

    # LA SOLUCIÓN: Apuntamos a 'LaPizarra/index.html' para evitar conflictos de nombres
    return render_template('LaPizarra/index.html', menu=menu, reviews=reviews)