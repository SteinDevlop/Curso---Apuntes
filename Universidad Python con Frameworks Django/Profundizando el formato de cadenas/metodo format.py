nombre = "Juan"
edad = 28
sueldo=45234
mensaje_formato="Mi nombre es {}, mi edad es {} y mi sueldo es {:.2f}".format(nombre,edad,sueldo)
print(mensaje_formato)
mensaje_formato = "Nombre {0} Edad {1} Sueldo {2:.2f}".format(nombre,edad,sueldo)
#con esto no importa el orden con el que se ponga los {} 
print(mensaje_formato)
mensaje_formato="Mi nombre es {n}, mi edad es {s} y mi sueldo es {r:.2f}".format(n=nombre,s=edad,r=sueldo)
print(mensaje_formato)
diccionario = {"nombre":"Ivan","Edad":43,"Sueldo":80000.00}
print(diccionario)