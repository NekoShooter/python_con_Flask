from wtforms import StringField, PasswordField, Form, validators



class LoginForm(Form):
    nombre = StringField('nombre',[validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    
    def damePassword(self) -> str:
        return self.password.data
    
    def dameNombre(self) -> str:
        return self.nombre.data

    def dameDatos(self) -> dict:
         return {'nombre' : self.dameNombre(),'email': self.dameNombre(), 'password' : self.damePassword()}



class RegistroForm(LoginForm):
    try:
        email = StringField('email', [validators.DataRequired(), validators.Email()])
    except:
        email = StringField('email', [validators.DataRequired()])

    def dameEmail(self) -> str:
        return self.email.data

    def dameDatos(self) -> dict:
         return {'nombre' : self.dameNombre(),'email': self.dameEmail(), 'password' : self.damePassword()}



class PendientesForm(Form):
    pendiente =  StringField('pendiente',[validators.DataRequired()])
    
    def dameTarea(self) -> str:
        return self.pendiente.data