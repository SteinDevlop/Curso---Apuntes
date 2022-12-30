from conexion import Conexion
from cursor_del_pool import CursorDelPool
from usuario import Usuario
from logger_base import log

class usuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'usuario insertada: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'usuario actualizada: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    #usuario1 = Usuario(username='Sanza', password='2431')
    #usuarios_insertadas = usuarioDAO.insertar(usuario1)
    #log.debug(f'usuarios insertadas: {usuarios_insertadas}')

    # Actualizar un registro
#    usuario1 = Usuario(1,"Sanchez","4234")
#    usuarios_actualizadas = usuarioDAO.actualizar(usuario1)
#    log.debug(f'usuarios actualizadas: {usuarios_actualizadas}')

    # Eliminar un registro
#    usuarios_eliminadas = usuarioDAO.eliminar(usuario1)
#    log.debug(f'usuarios eliminadas: {usuarios_eliminadas}')

    # Seleccionar objetos
    usuarios = usuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)