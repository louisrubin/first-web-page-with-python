from flask import Flask, render_template, request
from conversiones_main import *

app = Flask(__name__)


@app.route('/', methods=['GET','POST','PUT'])     # la barra sin ningun nombre indica la ruta raíz
def POST():                # llama un metodo 'principal'
    #return render_template('index.html')    # que retorna una plantilla (template) el cual es 'index.html'
    if request.method == 'POST':
        numero = request.form['numero']
        base_origen = request.form['base_origen']
        base_a_convertir = request.form['base_a_convertir']
        print(numero)
        print(base_origen)
        print(base_a_convertir)
        return 'received index'
    else:
        return 'not post'

@app.route('/lenguajes')
def mostrar_lenguajes():
    return render_template('lenguajes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)