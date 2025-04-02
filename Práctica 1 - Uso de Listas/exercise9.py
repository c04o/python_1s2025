"""
9. Escribe un programa que recorra una lista de cadenas y elimine aquellas
que estén vacías. Imprime la lista resultante.
"""

l = ["Hola,", "", "mundo!", " ", "Python", "", "genial"]

r = [c for c in l if c.strip() != ""]
print(r)