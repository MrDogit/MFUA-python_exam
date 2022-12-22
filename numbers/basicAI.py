import random
def perceptron(sensor, weight, b=7):
    s = 0
    n_sensor = len(sensor)

    for i in range(n_sensor):
        s+=int(sensor[i]) * weight[i]
    if s >= b:
        return True
    else:
        return False

def decrease(number, weight):
    n_sensor = len(number)
    tmp_weight = weight.copy()
    for i in range(n_sensor):
        if int(number[i])==1:
            tmp_weight[i]-=1
    return tmp_weight

def increase(number, weight):
    n_sensor = len(number)
    tmp_weight = weight.copy()
    for i in range(n_sensor):
        if int(number[i])==1:
            tmp_weight[i]+=1
    return tmp_weight


NoDefault = lambda: object()
def teaching(num_index, num_list_example, weight, key = NoDefault, n = 100000):
    if not key is NoDefault:
        weightkey = weight[key]
    n_sensor = len(num_list_example[0])
    for i in range(n):
        j = random.randint(0, 9)
        if 'weightkey' in locals():
            r = perceptron(num_list_example[j], weight[key])
        else:
            r = perceptron(num_list_example[j], weight)
        if j != num_index:
            if r:
                if 'weightkey' in locals():
                    weight[key] = decrease(num_list_example[j], weight[key])
                else:
                    weight = decrease(num_list_example[num_index], weight)
        else:
            if not r:
                if 'weightkey' in locals():
                    weight[key] = increase(num_list_example[num_index], weight[key])
                else:
                    weight = increase(num_list_example[num_index], weight)