plantilla_contexto = {
    'btn_txt': None,
    'form': None,
    'fn': None,
    'nombre': None,
    'tareas': None,
    'id_tareas': None}

class PagContexto:
    pag_contexto = plantilla_contexto.copy()

    def __init__(self,usuario: object = None, funcion: str = None, formulario : object = None, txt_submit : str = None) -> None:
        self.funcion(funcion)
        self.Usuario(usuario)
        self.formulario(formulario, txt_submit)
        
        

    def funcion(self,nombre_de_la_funcion : str):
        if type(nombre_de_la_funcion) != str:
            return
        self.pag_contexto['fn'] = nombre_de_la_funcion
    

    
    def Usuario(self,usuario : object) -> None:

        try:
            usuario.cargarPendientes()
            self.pag_contexto['nombre'] = usuario.nombre
            self.pag_contexto['tareas'] = usuario.lista_tareas
            self.pag_contexto['id_tareas'] = usuario.ids_tareas
        except AttributeError:
            self.pag_contexto['nombre'] = None
            self.pag_contexto['tareas'] = None
            self.pag_contexto['id_tareas'] = None



    def formulario(self,form : object, txt_submit : str):
        if form:
            self.pag_contexto['form'] = form

        if type(txt_submit) == str:
            self.pag_contexto['btn_txt']= txt_submit
