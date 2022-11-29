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
else: # como en los elif y else, este se ejecuta cuando ninguna excepcion a sido encontrada
    print("No se encontro ningun error")
finally: #se ejecuta siempre, pero podemos llamarlo, esto indica que el try, finalizo
    print("Ejecucion Try, except ; Finalizado")
print(f"Resultado: {res}")
print("Codigo continua ...")
