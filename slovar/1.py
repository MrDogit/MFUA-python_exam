slovar = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 5, 'e' : 0 }
minZnachenie = 0
maxZnachenie = 0
for klyuch, znachenie in slovar.items():
    if znachenie <= minZnachenie:
        minZnachenie = znachenie
        minKlyuch = klyuch
    if znachenie >= maxZnachenie :
        maxZnachenie = znachenie
        maxKlyuch = klyuch
print("max", maxKlyuch, maxZnachenie, "min", minKlyuch, minZnachenie)