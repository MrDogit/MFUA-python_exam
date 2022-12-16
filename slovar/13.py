slovar = { 'Familia_Rabotnika1' : ['russkiy', 'angliskiy', 'cheshskiy'], 'Familia_Rabotnika2' :  ['russkiy', 'angliskiy', 'bolgarskiy'], 'Familia_Rabotnika3' : ['kitayskiy'], 'Familia_Rabotnika4' :  ['russkiy']}
slovar_schetchic_yazikov = dict()
max_vstrechetsa = 0
topovie_yaziky = []
for i in slovar.values():
    for ii in i:
        slovar_schetchic_yazikov[ii] = slovar_schetchic_yazikov.get(ii, 0) + 1
for i in slovar_schetchic_yazikov.values():
    if i > max_vstrechetsa:
        max_vstrechetsa = i
for i, ii in slovar_schetchic_yazikov.items():
    if ii == max_vstrechetsa:
        topovie_yaziky.append(i)
print(topovie_yaziky)
print(slovar_schetchic_yazikov.keys())
