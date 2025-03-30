paragraph = "Uno. Dos. Tres."
sentences = len(paragraph.split("."))

if paragraph[-1] == ".":
    sentences -= 1

print(f"The paragraph has {sentences} sentence(s)")