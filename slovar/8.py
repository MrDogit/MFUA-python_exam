slovar1 = { 'klyuch1': 1, 'klyuch3': 3 }
slovar2 = { 'klyuch1': 1, 'klyuch2': 2 }
obshiy_slovar = dict()
razniy_slovar = dict()

for klyuch1 in slovar1.keys():
    for klyuch2, znachenie in slovar2.items():
        if klyuch1 == klyuch2:
            obshiy_slovar[klyuch1] = znachenie
            
for obshiy_klyuch in obshiy_slovar.keys():
    for klyuch, znachenie in slovar1.items():
        if obshiy_klyuch != klyuch:
            razniy_slovar[klyuch1] = znachenie
    for klyuch, znachenie in slovar2.items():
        if obshiy_klyuch != klyuch:
            razniy_slovar[klyuch] = znachenie
        
print(razniy_slovar)