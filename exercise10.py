"""
10. Escribe un programa que recorra una lista de cadenas y cuente cuántas
veces aparece un carácter específico en cada cadena. Al final, muestra el
conteo para cada cadena.
"""

l= ["Hola,", "mundo!", "Python", "es", "genial"]
ch = "o"

for i, c in enumerate(l):
    co = c.count(ch)
    print(f"Cadena '{c}': {co} ocurrencias de '{ch}'")