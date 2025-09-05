
# evaluacion 7/10 
# aportes: ----  usar lower() para filtrar input usuario 
#          ----  usar try: -except para filtrar entrada solo numerica 
#          ----  el while cerrarlo con un break en ves de variable

#correciones

import random

def game_mind():
    print("La cpu ha escogido un numero del 1 al 100 adivinalo")
            #Creacion de variables para el juego
    cpu_valor = random.randint(1, 100)
    
    while True:
        try:
            player_valor = int(input("Ingresa un numero del 1 al 100: "))
        except ValueError:
            print("entrada no valida, ingrese un numero entero. ")
            continue

        if(cpu_valor == player_valor):
            print("excelente has ganado el juego")
            break
        elif(player_valor < cpu_valor):
            print("estas muy abajo de la opcion correcta")
        else:
            print("estas muy arriba de la opcion correcta")
            

#funcion de la llamada al juego
#game_mind(cpu_number, player_number)

def menu_game():   
    
    while True:  #uso de el True para whilke ----
        print("Eres capaz de Adivinar el numero correcto?")
        opcion_game = input("deseas jugar? SI/NO: ").lower() # uso del lower ------
        
        if(opcion_game == "no"):
            print("Hasta la proxima")
            break # uso de el break para cerrar ----
        elif(opcion_game == "si"):
            print("Juguemos")
            game_mind()
        else:
            print("esa no es una opcion valida")
            continue


#funcion de inicio de juego
menu_game()

