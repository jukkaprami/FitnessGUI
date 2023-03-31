weather = input('Mitä sääennuste lupaa? (vettä/lunta/aurinkoista)')
#Ensimmäinen ehto
if(weather=='vettä'):
    print('Muista sateenvarjo!')
#Toinen ehto
if(weather=='lunta'):
    print('Muista hanskat')
#Kolmas ehto
if(weather=='aurinkoista'):
    print('Muista aurinkolasit')
#Muutoin
else:
    print('Etsi sopivat varusteet, ei vettä, lunta, eikä aurinkoista')
