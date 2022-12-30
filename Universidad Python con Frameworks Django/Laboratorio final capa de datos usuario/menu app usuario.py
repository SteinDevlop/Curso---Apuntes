from conexion import Conexion as con
from cursor_del_pool import CursorDelPool as cur_pool
from logger_base import log as log
from usuario_dao import usuarioDAO
from usuario import Usuario

eleccion_tipo = None
while eleccion_tipo != 4:
    print("".center(50,"-"))
    print("""
    1) Listar usuario
    2) Agregar usuario
    3) Actualizar usuario
    4) Eliminar usuario
    5) Salir
    """)
    print("".center(50,"-"))
    try:
        eleccion_tipo = int(input(f"(1/2/3/4/5): "))
    except Exception as e:
        print(f"Error encontrado tipo:{type(e)}")
    if eleccion_tipo == 1:
        try:
            usuarios = usuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(usuario)
        except Exception as e:
            print(f"Error encontrado tipo:{type(e)}")
    elif eleccion_tipo == 2:
        try:
            print("".center(50,"-"))
            print("Iniciando proceso de agregar usuario")
            agr_user = input("Indique el nuevo nombre de usuario: ")
            agr_pass = input("Indique la nueva contraseña del usuario: ")
            user = Usuario(username=agr_user, password=agr_pass)
            insercion = usuarioDAO.insertar(user)
            log.info(f'Usuario: {agr_user}')
            print("".center(50,"-"))
        except Exception as e:
            print(f"Error encontrado tipo:{type(e)}")
        log.info(f'Usuario: {agr_user} insertado exitosamente.')
    elif eleccion_tipo == 3:
        try:
            print("".center(50,"-"))
            print("Iniciando proceso de actualizar usuario")
            act_id = int(input("Indique la id del usuario a actualizar: "))
            act_user = input("Indique el nuevo nombre de usuario: ")
            act_pass = input("Indique la nueva contraseña del usuario: ")
            user = Usuario(id_usuario=act_id,username=act_user,password=act_pass)
            actualizacion = usuarioDAO.actualizar(user)
            log.info(f'usuarios actualizadas: {actualizacion}')
            print("".center(50,"-"))
        except Exception as e:
            print(f"Error encontrado tipo:{type(e)}")
    elif eleccion_tipo == 4:
        try:
            print("".center(50,"-"))
            print("Iniciando proceso de eliminar a un usuario")
            del_id = int(input("Indique la id del usuario a eliminar: "))
            user = Usuario(id_usuario=del_id)
            eliminacion = usuarioDAO.eliminar(user)
            log.info(f'usuarios eliminados: {eliminacion}')
            print("".center(50,"-"))
        except Exception as e:
            print(f"Error encontrado tipo:{type(e)}")
    elif eleccion_tipo == 5:
        exit()