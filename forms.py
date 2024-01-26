from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class UserForm(Form):
    nombre = StringField("Nombre")
    email = EmailField("Correo Electronico")
    apaterno = StringField("Apaterno")
    materias  =SelectField("Materias", choices=[("Español",'Esp'),("Mat","Matemaricas"),("Ingles","ING")])
    radios = RadioField("Curso", choices=[("1","1"),("2","2"),("3","3"),("4","4")])

