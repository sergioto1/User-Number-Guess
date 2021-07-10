import random

def numberGuess(x):
    number_guess = random.randint(1,x)
    my_guess = 0
    while(my_guess != number_guess):
        my_guess = int(input("Lanza un número:\n"))
        if (my_guess > number_guess):
            print("Lo siento! Número muy alto.")
        elif (my_guess < number_guess):
            print("Lo siento! Número muy bajo.")
            
    print(f"Felicidades! Adivinaste el número. Es el {number_guess}.")

# Prueba
numberGuess(50)
