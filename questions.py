import random

words = ["python", "programa", "variable", "funcion", "bucle"]
word = random.choice(words)
guessed = []
attempts = 6
puntos = 100  # <--- Agregado

while attempts > 0:
    progress = "".join([l + " " if l in guessed else "_ " for l in word])
    print(f"\n{progress} | Puntos: {puntos}") # <--- Mostrar puntos
    if "_" not in progress:
        print(f"¡Ganaste! Puntaje final: {puntos}")
        break
    
    letter = input("Ingresá una letra: ").lower()
    if letter in word:
        guessed.append(letter)
    else:
        attempts -= 1
        puntos -= 10 # <--- Restar puntos
        print(f"Incorrecto. Puntos actuales: {puntos}")
