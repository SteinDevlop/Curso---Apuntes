from CreacióndeClasesdeExcepciónPersonalizadas import NumerosIdenticosException
res=None

try:
    a=int(input("Proporcione un entero para a: "))
    b=int(input("Proporcione un entero para b: "))
    if a == b:
        raise NumerosIdenticosException("Numeros Identicos") #raise para arrojar cualquier excepcion
    res=a/b 

except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e} , {type(e)}')
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {e} , {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {e} , {type(e)}")
else:
    print("No se encontro ningun error")
finally:
    print("Ejecucion Try, except ; Finalizado")
print(f"Resultado: {res}")
print("Codigo continua ...")
