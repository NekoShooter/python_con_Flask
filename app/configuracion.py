
class produccion(object):
    SECRET_KEY = 'llave super secreta'
    SQLALCHEMY_DATABASE_URI ='sqlite:///usurios.db'


class desarrollo(produccion):
    DEBUG = True