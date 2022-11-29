res=None

try:
    a=int(input("Proporcione un entero para a: "))
    b=int(input("Proporcione un entero para b: "))
    res=a/b #esta variable es local a este bloque de codigo
#podemos añadir multiples except
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e} , {type(e)}')
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {e} , {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {e} , {type(e)}")
print(f"Resultado: {res}")
print("Codigo continua ...")
