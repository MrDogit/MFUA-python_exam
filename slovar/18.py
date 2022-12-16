spisok_s_bukvami = [ 'a', 'b', 'c', 'd', 'e' ]
spisok_s_chislami = [ 1, 2, 3, 4, 5 ]
slovar = dict()

for i in range(len(spisok_s_bukvami)):
    slovar[spisok_s_bukvami[i]*3] = spisok_s_chislami[i]**2
print(slovar)
