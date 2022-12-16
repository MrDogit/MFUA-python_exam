slovar_celih_chisel = { 1:1, 2:2, 5:5, 7:7, 8:8, 9:9 }
otfiltrovanniy_slovar = dict()

for i, ii in slovar_celih_chisel.items():
    if ii**2 > 50:
        otfiltrovanniy_slovar[i] = ii
print(otfiltrovanniy_slovar)