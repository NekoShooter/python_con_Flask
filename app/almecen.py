from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

p = SQLAlchemy()

class Pendientes(p.Model):
    __tablename__ = 'pendientes'
    id = p.Column(p.Integer(), primary_key = True)
    id_usuario = p.Column(p.Integer())
    tarea = p.Column(p.String())
    creacion = p.Column(p.DateTime(), default= datetime.now)
    hecho = p.Column(p.Boolean(False))



    def __init__(self,usuario : object, tarea:str) -> None:
        if not tarea: return
        try:
            self.id_usuario = usuario.id
            self.tarea = tarea
        except:
            return



    @staticmethod
    def obtenerTareas(lista_id:list) -> list:
        lista = []
        for id in lista_id:
            pendiente = p.session.query(Pendientes).get(id)
            if pendiente:
                lista.append((pendiente.tarea, pendiente.hecho, id))
        return lista
        


    @staticmethod
    def __crear__(app) -> None:
        if not app: return
        p.init_app(app)
        with app.app_context():
            p.create_all()

            

    @staticmethod
    def agregarPendiente(usuario : object, pendiente:str) -> int or None:
        if type(pendiente) != str: return None

        tareaPendiente = Pendientes(usuario, pendiente)

        p.session.add(tareaPendiente)
        p.session.commit()
        return tareaPendiente.id



    @staticmethod
    def eliminar(id : int) -> bool:
        if type(id) != int or id <= 0: False
        p.session.query(Pendientes).filter(Pendientes.id == id).delete()
        p.session.commit()
        return True



    @staticmethod
    def cambiarEstado(usuario : object, id : int) -> None:
        tarea = p.session.query(Pendientes).get(id)

        if tarea and tarea.id_usuario == usuario.id:

            tarea.hecho = not tarea.hecho
            p.session.add(tarea)
            p.session.commit()



    @staticmethod
    def eliminarPorUsuario(usuario : object)->None:
        usuario.cargarIdsDePendientes()
        for id in usuario.ids_tareas:
            p.session.query(Pendientes).filter(Pendientes.id == id).delete()
        if len(usuario.ids_tareas) > 0:
            p.session.commit()