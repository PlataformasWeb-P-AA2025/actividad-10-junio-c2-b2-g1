from flask import Flask, render_template, request

app = Flask(__name__)

# Controlador: Ruta para manejar la página principal
@app.route('/', methods=['GET', 'POST'])
def hello():
    # Si el formulario es enviado con un nombre
    name = request.args.get('name', 'Invitado')  # Por defecto 'Invitado'
    
    # Vista: Renderiza la plantilla HTML con el nombre
    return render_template('hello.html', name=name)

# Arrancar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
