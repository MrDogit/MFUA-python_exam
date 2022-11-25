stroka = 'Hello World!'
slovar_stroki = dict()
for i in range(len(stroka)):
    slovar_stroki[stroka[i]] = slovar_stroki.get(stroka[i], 0) + 1

print(slovar_stroki.keys())