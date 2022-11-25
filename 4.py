glasnie = [ 'a', 'e', 'q', 'u', 'i', 'y', 'o', 'j' ]
soglasnie = [ 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
slovar = { 'glasnie':glasnie, 'soglasnie': soglasnie }
zadannaya_stroka = 'YES! SCIENCE!'
zadannaya_stroka = zadannaya_stroka.lower()
noviy_slovar = dict()
for i in range(len(zadannaya_stroka)):
    for ii in slovar['soglasnie']:
        if ii == zadannaya_stroka[i]:
            noviy_slovar[zadannaya_stroka[i]] = noviy_slovar.get(zadannaya_stroka[i], 0) + 1
print(noviy_slovar)