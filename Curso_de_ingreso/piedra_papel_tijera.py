import random

def play():
    print("Bienvenidos a Piedra, papel o tijera en Python")
    opcions = ["piedra", "papel", "tijera"]
    validacion = 's'

    while validacion == 's':
        computer_choice = random.choice(opcions)
        player = None

        while player not in opcions:
            player = input("\nPiedra, papel o tijera?: ").lower()

        # Opciones de victoria para el usuario
        cond1 = (player == "piedra" and computer_choice == "tijera")
        cond2 = (player == "papel" and computer_choice == "piedra")
        cond3 = (player == "tijera" and computer_choice == "papel")

        if cond1 or cond2 or cond3:
            print("La computadora eligió", computer_choice)
            print("¡Ganaste!")
        elif computer_choice == player:
            print("La computadora eligió", computer_choice)
            print("¡Empate!")
        else:
            print("La computadora eligió", computer_choice)
            print("¡Perdiste!")

        validacion = input("\nDesea seguir jugando? [S] Si - [CUALQUIER TECLA] No: ").lower()
        if validacion != 's':
            print("Gracias por jugar!.\n")
            break

play()