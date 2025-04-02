"""
3. Escribe un programa que recorra una lista de cadenas y convierta cada
cadena a mayúsculas o minúsculas dependiendo de un criterio. Si la
longitud de la cadena es par, se convertirá a mayúsculas; si es impar, a
minúsculas.
"""

l = ["Hola,", "mundo!", "Python", "es", "genial"]

r = [c.upper() if len(c) % 2 == 0 else c.lower() 
    for c in l]
print(r)