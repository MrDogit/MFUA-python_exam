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

num_index = 5
n_sensor = 15
# for i in range(n_sensor):
empty_weight = [0 for ii in range(n_sensor)]
full_weight = dict.fromkeys(['weight' + str(i) for i in range(len(numbers))], empty_weight)

def perceptron(sensor, weight):
    b = 7
    s = 0

    for i in range(n_sensor):
        s+=int(sensor[i]) * weight[i]
        # print(weight,'\n', sensor[i], weight[i], s)
    if s >= b:
        return True
    else:
        return False

def decrease(numbers, weight):
    tmp_weight = weight.copy()
    for i in range(n_sensor):
        if int(numbers[i])==1:
            tmp_weight[i]-=1
    return tmp_weight

def increase(numbers, weight):
    tmp_weight = weight.copy()
    for i in range(n_sensor):
        if int(numbers[i])==1:
            tmp_weight[i]+=1
    return tmp_weight


NoDefault = lambda: object()
def teaching(num_index, weight, key = NoDefault):
    if not key is NoDefault:
        weightkey = weight[key]
    n = 100000
    for i in range(n):
        j = random.randint(0, 9)
        if 'weightkey' in locals():
            r = perceptron(numbers[j], weight[key])
        else:
            r = perceptron(numbers[j], weight)
        if j != num_index:
            if r:
                if 'weightkey' in locals():
                    weight[key] = decrease(numbers[j], weight[key])
                else:
                    weight = decrease(numbers[num_index], weight)
        else:
            if not r:
                if 'weightkey' in locals():
                    weight[key] = increase(numbers[num_index], weight[key])
                else:
                    weight = increase(numbers[num_index], weight)
                    


# teaching(1, full_weight, 'weight1')
# print('\nOutput:\n', full_weight['weight1'])
print(full_weight)
for i in range(len(numbers)):
    teaching(i, full_weight, 'weight' + str(i))
    print(i, 'weight' + str(i), full_weight['weight' + str(i)])
    for ii in range(len(numbers)):
        perceptron_work = perceptron(numbers[i], full_weight['weight' + str(ii)])
        if i == ii and perceptron_work != True or i != ii and perceptron_work == True:
            print('NOT NICE :(')
            _nice = False
        if ((ii == len(numbers)-1 and not '_nice' in locals()) or ('_nice' in locals() and not _nice == False)):
            print('NICE :)')
print('\nweigt:', full_weight)
    
f_one = list('111100111001111')
# print(full_weight)
# for i in range(len(numbers)):
    # print(perceptron(numbers[i]))
# print(perceptron(f_one))