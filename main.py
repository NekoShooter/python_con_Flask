from app import crearAPP, login_manager
from app.usuarios import Usuario
from app.pag_contexto import PagContexto
from app.formularios import PendientesForm
from flask import render_template, request, redirect, url_for
from flask_login import login_required,current_user,logout_user

app = crearAPP()
Usuario.__crear__(app)


@login_manager.user_loader
def cargarUsuario(str_id) -> object or None:
    return Usuario.obtenerPorId(int(str_id))



@app.route('/')
@login_required
def inicio():
    ctx = PagContexto(usuario = current_user)
    return render_template('index.html',  **ctx.pag_contexto)



@app.route('/salir', methods =['GET', 'POST'])
@login_required
def salir():

    if request.method == 'POST':
        logout_user()
        return redirect(url_for('autenticacion.logearse'))

    ctx = PagContexto(usuario= current_user, 
                      txt_submit='salir',
                      funcion='salir')

    return render_template('salir.html',**ctx.pag_contexto)



@app.route('/agregar_pendientes', methods=['GET', 'POST'])
@login_required
def agregarPendientes():
    tareaForm = PendientesForm(request.form)
    
    if request.method == 'POST' and tareaForm.validate():
        current_user.agregarPendiente(tareaForm.dameTarea())

    ctx = PagContexto(funcion='agregarPendientes', 
                      formulario= tareaForm, 
                      txt_submit='agregar', 
                      usuario= current_user)

    return render_template('agregar_pendientes.html',**ctx.pag_contexto)



@app.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    current_user.eliminarPendiente(id)
    return redirect(url_for('agregarPendientes'))



@app.route('/hecho/<int:id>')
@login_required
def hecho(id):
    current_user.intercambiarPendienteHecho(id)
    return redirect(url_for('agregarPendientes'))



@app.errorhandler(404)
@app.errorhandler(500)
def error(Error):
    return render_template('error.html',err = Error.code)



if __name__ == '__main__':
    app.run()