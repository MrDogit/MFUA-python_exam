spisok = ['name1@domen1', 'name2@domen2', 'name3@domen3', 'name1@domen3']
slovar = dict()
for i in range(len(spisok)):
    vremenniy_spisok = spisok[i].split('@')
    try:
        slovar[vremenniy_spisok[1]].append(vremenniy_spisok[0])
    except KeyError:
        slovar[vremenniy_spisok[1]] = []
        slovar[vremenniy_spisok[1]].append(vremenniy_spisok[0])
print(slovar)