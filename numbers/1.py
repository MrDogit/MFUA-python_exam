import numbers
import numpy as np
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

numsbers = [one, two, three, four, five, six, seven, eight, nine, zero]

tema = 5
n_sensor = 15
w = [0 for i in range(15)]

def perceptron(sensor):
    b = 7
    s = 0

    for i in range(n_sensor):
            s+=int(sensor[i]) * w[i]
            if s >= b:
                return True
            else:
                return False

def decrease(numbers):
    for i in range(n_sensor):
        if int (numbers[i])==1:
            w-=1

def increase(numbers):
    for i in range(n_sensor):
        if int(numbers[i]):
            w+=1

n = 100000
for i in range(n):
    j = random.randint(0, 9) 
    r = perceptron(numbers[j])

    if j != tema:
        if r:  
            decrease(numbers[j])

    else:
        if not r:
            increase(numbers[tema])

print(w)
f_one = list('111100111001111')
print( perceptron(f_one))






