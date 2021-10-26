from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    return 'welcome'

@app.route('/contacto')
def contacto():
    return "esta es la pagina de contactos"
"""

@app.route('/')     # la barra sin ningun nombre indica la ruta raíz
def principal():                # llama un metodo 'principal'
    return render_template('index.html')    # que retorna una plantilla (template) el cual es 'index.html'

@app.route('/lenguajes')
def mostrar_lenguajes():
    return render_template('lenguajes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)