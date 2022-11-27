slovar_s_chislovimy_znacheniami = { 1:1, 5:5, 9:9, 10:10, 11:11, 100:100}
noviy_slovar = dict()

for i, ii in slovar_s_chislovimy_znacheniami.items():
    if ii < 10:
        noviy_slovar[i] = ii
        
print(noviy_slovar.keys())