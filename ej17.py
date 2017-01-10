unoADiecinueve = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
ty = [0,3,6,6,5,5,5,7,6,6]
Hundred = 7
Thousand = 8

 
total = 0
for i in range(1,1000):
    unidades = i % 10 
    decenas = int(((i % 100) - unidades) / 10 )
    centenas = int(((i % 1000) - (decenas * 10) - unidades) / 100)
 
    if centenas != 0:
        total += unoADiecinueve[centenas] + Hundred # "S[centenas] hundred
        if decenas != 0 or unidades != 0: total += 3 # "and"
    if decenas == 0 or decenas == 1: total += unoADiecinueve[decenas * 10 + unidades]
    else: total += ty[decenas] + unoADiecinueve[unidades]
 
total += unoADiecinueve[1] + Thousand

print(total)




