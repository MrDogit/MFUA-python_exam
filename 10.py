slovar = { 'klyuch1': 1, 'klyuch3': 3, 'klyuch2': 2 }
slozhennie_chisla = 1
minZnachenie = -1
maxZnachenie = 0
for znachenie in slovar.values():
    if znachenie <= minZnachenie or minZnachenie == -1:
        minZnachenie = znachenie
    if znachenie >= maxZnachenie :
        maxZnachenie = znachenie
slozhennie_chisla = minZnachenie + maxZnachenie
print(slozhennie_chisla)