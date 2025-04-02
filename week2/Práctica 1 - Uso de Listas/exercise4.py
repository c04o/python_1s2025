"""
4. Escribe un programa que busque si una sub cadena está presente en cada
una de las cadenas de una lista. El programa debe devolver una lista con
valores booleanos que indiquen si la sub cadena fue encontrada en cada
cadena.
"""

l = ["Hola,", "mundo!", "Python", "es", "genial"]
sc = "o"

r = [sc in c for c in l]
print(r)