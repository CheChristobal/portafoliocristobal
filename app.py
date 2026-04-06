import os
import importlib
from flask import Flask, render_template

app = Flask(__name__)

# Configuración de ruta absoluta para evitar errores de ejecución
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTOS_DIR = os.path.join(BASE_DIR, 'proyectos')

def registrar_proyectos():
    proyectos_encontrados = []
    
    # Verificamos que la carpeta proyectos exista
    if not os.path.exists(PROYECTOS_DIR):
        print("⚠️ Carpeta 'proyectos' no encontrada.")
        return []

    for folder in os.listdir(PROYECTOS_DIR):
        path = os.path.join(PROYECTOS_DIR, folder)
        
        # Filtramos: Solo carpetas que no sean del sistema (__pycache__, etc)
        if os.path.isdir(path) and not folder.startswith('__'):
            try:
                # Importación dinámica del módulo app.py de cada subproyecto
                module = importlib.import_module(f"proyectos.{folder}.app")
                
                # Buscamos el Blueprint dentro del módulo
                for attr in dir(module):
                    bp = getattr(module, attr)
                    
                    # Condición: El objeto debe terminar en _bp (ej: tele_pollo_bp)
                    if attr.endswith('_bp'):
                        # Registramos el Blueprint en la app principal
                        app.register_blueprint(bp, url_prefix=f'/{folder}')
                        
                        # Agregamos a la lista para el renderizado del portafolio
                        # Formateamos el nombre para que luzca bien (ej: "la_pizarra" -> "LA PIZARRA")
                        proyectos_encontrados.append({
                            'id': folder,
                            'titulo': folder.replace('_', ' ').upper(), 
                            'endpoint': f'{bp.name}.index'
                        })
                        print(f"✅ Módulo '{folder}' cargado exitosamente.")
                        break
            except Exception as e:
                print(f"❌ Error en módulo {folder}: {e}")
                
    return proyectos_encontrados

# Ejecución del escáner de proyectos
MIS_PROYECTOS = registrar_proyectos()

@app.route('/')
def index():
    # Renderizamos la página principal con la lista de proyectos dinámicos
    return render_template('index_principal.html', proyectos=MIS_PROYECTOS)

if __name__ == '__main__':
    # Ejecución en modo debug para desarrollo
    app.run(debug=True, port=5000)