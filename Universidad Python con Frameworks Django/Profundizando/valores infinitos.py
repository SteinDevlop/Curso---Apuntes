#Valores infinitos
import math
from decimal import Decimal 
#Importamos math para verificar si un valor es infinito
infinity_positive = float("inf")
#print(infinity_positive)
#print(f"Es infinito: {math.isinf(infinity_positive)}")


infinity_negative = float("-inf")
#print(infinity_negative)
#print(f"Es infinito: {math.isinf(infinity_negative)}")

"""
Otras formas
"""

infinity_positive = math.inf
#print(f"Valor:{infinity_positive}")
#print(f"Es infinito?: {math.isinf(infinity_positive)}")

infinity_negative = -math.inf
#print(f"Valor:{infinity_negative}")
#print(f"Es infinito?: {math.isinf(infinity_negative)}")

infinity_positive = Decimal("Infinity")
print(f"Valor:{infinity_positive}")
print(f"Es infinito?: {math.isinf(infinity_positive)}")

infinity_positive = Decimal("-Infinity")
print(f"Valor:{infinity_positive}")
print(f"Es infinito?: {math.isinf(infinity_positive)}")