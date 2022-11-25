anglo_russkiy = {'hello' : 'privet', 'world' : 'mir', 'dictionary' : 'slovar'}
anglo_nemeckiy = {'hello' : 'hallo', 'world' : 'welt', 'power': 'energie'}
russko_nemeckiy = dict()
for i, ii in anglo_russkiy.items():
    for iii, iiii in anglo_nemeckiy.items():
        if i == iii:
            russko_nemeckiy[ii] = iiii
print(russko_nemeckiy)