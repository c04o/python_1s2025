"""
5. Escribe un programa que recorra una lista de cadenas y reemplace todas
las apariciones de un carácter específico con otro carácter, luego imprime la
lista modificada.
"""

l = ["Hola,", "mundo!", "Python", "es", "genial"]
c_viejo = "o"
c_nuevo = "x"

r = [c.replace(c_viejo, c_nuevo) for c in l]
print(r)