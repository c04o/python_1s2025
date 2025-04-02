"""
7. Escribe un programa que recorra una lista de cadenas y divida cada cadena
en subcadenas utilizando un delimitador específico (por ejemplo, una coma
o un espacio).
"""

l = ["Hola,mundo!", "Python,es,genial", "programación", "a,b,c"]
d = ","

r = [c.split(d) for c in l]
print(r)