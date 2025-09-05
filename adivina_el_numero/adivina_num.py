#Mi recomendación es que empieces con el juego Adivina el Número. 
# Es un clásico para principiantes porque te permite practicar 
# conceptos fundamentales del lenguaje como variables, condicionales (if/else), 
# bucles (while), y la entrada/salida de datos.

#¿Cómo funciona el juego?

# El juego Adivina el Número es bastante simple:

    # La computadora elige un número secreto aleatorio entre 1 y 100.

    # El jugador tiene que adivinar cuál es ese número.

    # Después de cada intento, el programa le dice al jugador si su suposición es demasiado alta o demasiado baja.

    # El juego continúa hasta que el jugador adivina correctamente el número.

import random

def game_mind(cpu_valor, player_valor):
    #parte cenral del juego
    tope = True
    while tope:
        if(cpu_valor == player_valor):
            print("excelente has ganado el juego")
            tope = False
        elif(player_valor < cpu_valor):
            print("estas muy abajo de la opcion correcta")
            player_valor = int(input("Ingresa otro numero del 1 al 100: "))
            continue
        elif(player_valor > cpu_valor):
            print("estas muy arriba de la opcion correcta")
            player_valor = int(input("Ingresa otro numero del 1 al 100: "))
            continue
        else:
            print("Uyy, algo salio mal")
            continue



#funcion de la llamada al juego
#game_mind(cpu_number, player_number)

def menu_game():   
    tope = True
    while tope:
        print("Eres capaz de Adivinar el numero correcto?")
        opcion_game = input("deseas jugar? SI/NO")
        if(opcion_game == "no" or opcion_game == "NO" or opcion_game == "No" or opcion_game == "nO"):
            print("Hasta la proxima")
            tope = False
        elif(opcion_game == "si" or opcion_game == "SI" or opcion_game == "Si" or opcion_game == "sI"):
            print("Juguemos")
            print("La cpu ha escogido un numero del 1 al 100 adivinalo")
            #Creacion de variables para el juego
            cpu_number = random.randint(1, 100)
            player_number = int(input("Ingresa un numero del 1 al 100: "))
            game_mind(cpu_number, player_number)
        else:
            print("esa no es una opcion valida")
            continue


#funcion de inicio de juego
menu_game()

# evaluacion 7/10 
# aportes: ----  usar lower() para filtrar input usuario 
#          ----  usar try: -except para filtrar entrada solo numerica 

#correciones

