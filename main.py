from flask import Flask,request,render_template,Response
from flask_wtf.csrf import CSRFProtect

from flask import flash,g

import forms

app = Flask(__name__)

app.secret_key = 'ESTA ES LA CLAVE SECRETA'

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/")
def index():
    return render_template("index.html")

@app.before_request
def before_request():
    g.prueba = "Hola"
    print("Antes 1")

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    print("dentro2")
    valor = g.prueba
    print("valor de g.prueba",valor)
    nom =''
    apa=''
    ama=''
    alum_form  =forms.UserForm(request.form)
    if request.method == 'POST':
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("apterno: {}".format(apa))
        print("amaterno: {}".format(ama))


#archivo_texto.write('\n datos en el archivo')
    return render_template("alumnos.html", form=alum_form,nom=nom,apa=apa,ama=ama)
    
@app.after_request
def after_request(response):
    print("Despues de la petición")
    return response

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/datos")
def hola():
    return "<p> Hola Mundo <p>"

@app.route("/hola")
def func():
    return "<h1> Saludo desde UTL </h1>"

@app.route("/saludo")
def func1():
    return "<h1> Saludo desde Saludo </h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1> Hola </h1>" + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1> El numero es {} <h1>".fromat(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(nom,id):
    return "<h1> ID {}, NOMBRE: {} <h1>".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return " La suma de {} + {} = {} ".format(n1,n2,n1+n2)

@app.route("/mulitiplica",methods=["GET","POST"])
def mult():
        if request.method == "POST":
            n1 = request.get["n1"]
            n2 = request.get["n2"]
            return  "<h1> El resultado es : {} </h1>".format(str(int(n1)*int(n2)))
        else:
            return '''
                <form action="/mulitiplica" method="POST">
                    <laber> Numero 1 </label>
                    <input type="text" name="n1">
                    <label> Numero 2 </label>
                    <input type="text" name="n2">
                    <input type="submit">
                </form>
'''
@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado",methods=["GET","POST"])
def mult1():
        if request.method == "POST":
            n1 = request.form.get("n1")
            n2 = request.form.get("n2")
            return  "<h1> El resultado es : {} </h1>".format(str(int(n1)*int(n2)))

if __name__ == "__main__":
    app.run(debug=True)