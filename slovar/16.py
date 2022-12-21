zadannaya_stroka = "Hello world!"
slovar = { 'h':0, 'l':1, 'd':8}

def kodirovshik(stroka):
    novaya_stroka = stroka
    for i in range(len(stroka)):
        for ii, iii in slovar.items():
            if stroka[i] == ii:
                novaya_stroka[i] = iii
    return novaya_stroka

print(kodirovshik(zadannaya_stroka))