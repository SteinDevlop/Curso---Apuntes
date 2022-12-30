from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
            Id usuario: {self._id_usuario},
            username: {self._username},
            password: {self._password}
        '''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return  self._password

    @password.setter
    def password(self, password):
        self._password = password

if __name__ == '__main__':
    persona1 = Usuario(1, 'Juan', 'Perez')
    log.debug(persona1)
    # Simular un insert
    persona1 = Usuario(username='Juan', password='Perez')
    log.debug(persona1)
    # Simular un delete
    persona1 = Usuario(id_usuario=1)
    log.debug(persona1)