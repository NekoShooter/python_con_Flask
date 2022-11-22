from flask import redirect, url_for, render_template, request, flash
from app.usuarios import Usuario
from app.formularios import LoginForm, RegistroForm
from app.pag_contexto import PagContexto
from flask_login import login_user, current_user, login_required, logout_user
from . import autenticacion



@autenticacion.route('login', methods = ['GET', 'POST'])
def logearse():
    if current_user.is_authenticated:
        return redirect(url_for('salir'))

    login = LoginForm(request.form)

    if request.method == 'POST' and login.validate() :
        usuario_logeado = Usuario.logearse(login.dameDatos())

        if usuario_logeado:
            login_user(usuario_logeado)
            return redirect(url_for('inicio'))
            
        flash('usuario o contraseña incorrectos')

    ctx = PagContexto(formulario=login, txt_submit= 'login', funcion='autenticacion.logearse')

    return render_template('form.html', **ctx.pag_contexto)
    


@autenticacion.route('registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('inicio'))

    registrar = RegistroForm(request.form)

    if request.method == 'POST' and registrar.validate():
        nuevoUsuario = registrar.dameDatos()

        if Usuario.agregarUsuarios(nuevoUsuario):
            login_user(Usuario.logearse(nuevoUsuario))
            return redirect(url_for('inicio'))

    elif request.method == 'POST':
        flash('Datos ingresados incorrectos')

    ctx = PagContexto(formulario=registrar, txt_submit= 'registrarse', funcion='autenticacion.registro')

    return render_template('form.html', **ctx.pag_contexto)



@autenticacion.route('eliminar_cuenta', methods=['GET', 'POST'])
@login_required
def eliminar_cuenta():

    if request.method == 'POST':
        Usuario.eliminarUsuario(current_user)
        logout_user()
        return redirect(url_for('inicio'))

    ctx = PagContexto(usuario = current_user, txt_submit= 'Eliminar', funcion='autenticacion.eliminar_cuenta')

    return render_template('salir.html',**ctx.pag_contexto)