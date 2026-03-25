import random

words = ["python", "programa", "variable", "funcion", "bucle"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    progress = "".join([l + " " if l in guessed else "_ " for l in word])
    print(progress)
    if "_" not in progress:
        print("¡Ganaste!")
        break
    
    letter = input("Ingresá una letra: ").lower()
    if letter in word:
        guessed.append(letter)
    else:
        attempts -= 1
        print(f"Incorrecto. Te quedan {attempts} intentos.")
