slovar = { 'b' : 2, 'c' : 3, 'd' : 5, 'e' : 0}
minValue = 0
maxValue = 0
for key, value in slovar.items():
    if value <= minValue:
        minValue = value
        minKey = key
    if value >= maxValue :
        maxValue = value
        maxKey = key
print("max", maxKey, maxValue, "min", minKey, minValue)
if slovar.get('f', 1):
    slovar['a'] = slovar.get('a', 0) + 1
    print("test")
    print(slovar.items())