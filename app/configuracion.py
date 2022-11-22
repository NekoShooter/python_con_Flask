
class produccion(object):
    SECRET_KEY = 'llave super secreta'


class desarrollo(produccion):
    SQLALCHEMY_DATABASE_URI ='sqlite:///usurios.db'
    DEBUG = True