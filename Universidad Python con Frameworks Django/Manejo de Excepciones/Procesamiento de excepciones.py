res = None
#a = "sd"
a=10
b = 0
try:
    res=a/b
#except ZeroDivisionError as e:
#    print(f"Ocurrio un error: {e}")
except Exception as e:
    print(f"Ocurrio un error: {e}")

print(f"Resultado: {res}")
print("Codigo continua ...")