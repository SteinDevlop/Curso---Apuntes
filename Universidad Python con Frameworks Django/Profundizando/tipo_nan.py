import math
from decimal import Decimal
#dato numerico que no es un numero y no tiene valor numerico definido
a= float("NaN")
print(f"Es NaN (not a number)?: {math.isnan(a)}")

a= Decimal("NaN")
print(f"Es NaN (not a number)?: {math.isnan(a)}")