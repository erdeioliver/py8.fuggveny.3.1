'''
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''

lista = [3, 5, 6, 8, 12, 18, 21, 22]

def harommal_oszthatok(listacska):
    szamlalo = 0
    for i in listacska:
        if i % 3 == 0:
            szamlalo += 1
    return print(szamlalo) 


harommal_oszthatok(lista)