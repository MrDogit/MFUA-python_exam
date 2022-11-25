testoviy_spisok = [ 1, 2, 3, 4, 5 ]
def to_dict(lst):
    slovar = dict()
    for i in lst:
        slovar[i] = i
    return slovar
print(to_dict(testoviy_spisok))