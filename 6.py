import random
random.randint(0,9)
stroka_iz_cifr = ''
for i in range(random.randint(10,10)):
    stroka_iz_cifr = stroka_iz_cifr + str(random.randint(0,9))
    
def count_it(sequence):
    slovar = dict()
    for i in range(len(sequence)):
        slovar[sequence[i]] = slovar.get(sequence[i], 0) + 1
    top1znachenie = -1
    top1klyuch = -1
    top2znachenie = -1
    top2klyuch = -1
    top3znachenie = -1
    top3klyuch = -1
    vremenniy_slovar = slovar.copy()
    
    for klyuch, znachenie in vremenniy_slovar.items():
        if znachenie > top1znachenie:
            top1znachenie = znachenie
            top1klyuch = klyuch
        elif znachenie > top2znachenie:
            top2znachenie = znachenie
            top2klyuch = klyuch
        elif znachenie > top3znachenie:
            top3znachenie = znachenie
            top3klyuch = klyuch
            
    for klyuch in vremenniy_slovar.keys():
        if klyuch != top1klyuch and klyuch != top2klyuch and klyuch != top3klyuch:
            slovar.pop(klyuch)
    return slovar

print(stroka_iz_cifr)
print(count_it(stroka_iz_cifr))