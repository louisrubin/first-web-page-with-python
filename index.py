from flask import Flask, render_template

app = Flask(__name__, static_url_path='/templates/static')


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