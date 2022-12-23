import multiprocessing as mp
# import numpy as np
from basicAI import teaching, perceptron

n_example = list('000000000000000')
zero =  list('111101101101111')
one =   list('001001001001001')
two =   list('111001111100111')
three = list('111001111001111')
four =  list('101101111001001')
five =  list('111100111001111')
six =   list('111100111101111')
seven = list('111001001001001')
eight = list('111101111101111')
nine =  list('111101111001111')
numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

empty_weight = [0 for i in range(len(numbers[0]))]
full_weight = dict.fromkeys(['weight' + str(i) for i in range(len(numbers))], empty_weight)

def smth(i):
    teaching(i, numbers, full_weight, 'weight' + str(i))
    print(i, 'weight' + str(i), full_weight['weight' + str(i)])
    for ii in range(len(numbers)):
        perceptron_work = perceptron(numbers[i], full_weight['weight' + str(ii)])
        if i == ii and perceptron_work != True or i != ii and perceptron_work == True:
            print('NOT NICE :(')
            _nice = False
        if ((ii == len(numbers)-1 and not '_nice' in locals()) or ('_nice' in locals() and not _nice == False)):
            print('NICE :)')

# print(full_weight)
# mp.set_start_method('spawn')
queue = mp.Queue()
processes = [mp.Process(target=smth, args=(i)) for i in range(len(numbers))]

for p in processes:
    p.start()

for p in processes:
    p.join()
    
    

print('\nweigt:', full_weight)
    
f_one = list('111100111001111')
# print(full_weight)
# for i in range(len(numbers)):
    # print(perceptron(numbers[i]))
# print(perceptron(f_one))