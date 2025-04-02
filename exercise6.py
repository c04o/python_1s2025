"""
6. Escribe un programa que recorra una lista de cadenas y elimine los
espacios en blanco al principio y al final de cada cadena
"""

l = ["  Hola,  ", "mundo! ", "  Python", " es ", "genial  "]

r = [c.strip() for c in l]
print(r)