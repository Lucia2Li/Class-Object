from ejercicio_1 import Dice

#Crear dos dados
die1 = Dice()
die2 = Dice()

for idx in range(5):
    roll1 = die1.roll()
    roll2 = die2.roll()
    print(f'Die1 = {roll1} and Die2 = {roll2}' )

#Crear un bucle que te permita hacer los dos dados