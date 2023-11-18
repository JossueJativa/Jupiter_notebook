import random

'''
Un tren y un bus llegan a una estación de forma aleatoria entre 8h00 y 9h00.  
El tren para en la estación por 10 minutos y el bus por X minutos.  
Encuentre el valor de X para que la probabilidad del tren y el bus encontrarse 
en la estación sea 0.5.
'''
# Probabilidad de que el tren y el bus se encuentren en la estacion es 0.5
# dar un ramdom que este entre 800 y 900
x = 1
trys = 1
coincident = 0
probability = 0

while probability == 0.5:
    TrainArrive = random.randint(800, 860)

    TrainWait = TrainArrive + 10

    busArrived = random.randint(800, 860)

    busWait = busArrived + x
    
    # Si el tren llega el bus a llegado es que hay una coincidencia
    # y si el tren esta esperando el bus arrivo hay una coincidencia
    if busArrived >= TrainArrive and busArrived <= TrainWait:
        coincident += 1
    else:
        if busWait >= TrainArrive and busWait <= TrainWait:
            coincident += 1
        else:
            trys += 1
            x += 1


print(f"The minuts to waits on bus is: {x}")
print(f"The coinsident is: {coincident}")
probability = coincident / trys