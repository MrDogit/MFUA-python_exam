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

n_sensor = 15

empty_weight = [0 for ii in range(n_sensor)]
full_weight = dict.fromkeys(['weight' + str(i) for i in range(len(numbers))], empty_weight)

def smth(weight):
    tmp_weight = weight.copy()
    tmp_weight[1] += 1
    print(tmp_weight)
    print(weight)
    return tmp_weight

print(full_weight, '\n')
full_weight['weight1'] = (smth(full_weight['weight1']))
smth(full_weight['weight1'])
print('\n', full_weight)