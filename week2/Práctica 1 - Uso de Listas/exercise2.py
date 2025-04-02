"""
2. Escribe un programa que recorra una lista de cadenas y calcule la longitud
de cada cadena, almacenando el resultado en una nueva lista.
"""

l = ["Hola,", "mundo!", "Python", "es", "genial"]

lo = [len(c) for c in l]
print(lo)