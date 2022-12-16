# import numpy as np
import random

one =   list('001001001001001')
two =   list('111001111100111')
three = list('111001111001111')
four =  list('101101111001001')
five =  list('111100111001111')
six =   list('111100111101111')
seven = list('111001001001001')
eight = list('111101111101111')
nine =  list('111101111001111')
zero =  list('111101101101111')

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

tema = 5
n_sensor = 15
# for i in range(n_sensor):
empty_weight = [0 for ii in range(n_sensor)]
weight = dict.fromkeys(['weight' + str(i) for i in range(len(numbers))], empty_weight)

def perceptron(sensor, weight):
    b = 7
    s = 0

    for i in range(n_sensor):
        s+=int(sensor[i]) * weight[i]
    if s >= b:
        return True
    else:
        return False

def decrease(numbers, weight):
    for i in range(n_sensor):
        if int (numbers[i])==1:
            weight[i]-=1

def increase(numbers, weight):
    for i in range(n_sensor):
        if int(numbers[i])==1:
            weight[i]+=1

n = 100000
def teaching(weight, tema):
    for i in range(n):
        j = random.randint(0, 9) 
        r = perceptron(numbers[j], weight)

        if j != weight:
            if r:  
                decrease(numbers[j], weight)

        else:
            if not r:
                increase(numbers[5], weight)

print(weight)
teaching(weight['weight1'], 1)
print(weight)
f_one = list('111100111001111')
# for i in range(len(numbers)):
    # print(perceptron(numbers[i]))
# print(perceptron(f_one))






