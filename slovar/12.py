spisok1 = [ 1, 2, 3 ]
spisok2 = [ 4, 5, 6 ]
slovar = dict()
for i in range(len(spisok1)):
    slovar[spisok1[i]] = spisok2[i]
print(slovar)