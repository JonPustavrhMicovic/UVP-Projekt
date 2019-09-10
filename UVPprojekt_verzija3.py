import numpy as np
import os

#numpy za lažjo predstavitev matrike aka plošče
#os za končanje programa

#globalne spremenljivke
STEVILO_VRSTIC = 6
STEVILO_STOLPCEV = 7
POTEZA = 0

konec_igre = False

zeton_igralca_1 = 1
zeton_igralca_2 = 2

#MODEL

#spremeni desko tam kjer igralec postavi zeton
def igralna_poteza(deska, vrstica,stolpec,zeton):
    deska[vrstica][stolpec] = zeton

#preveri ali je stolpec prazen
def dovoljena_poteza(deska, stolpec):
    return deska[0][stolpec] == 0

#poišči prvo prazno vrstico za izbran stolpec
def prva_prazna_vrstica(deska, stolpec):
    vrstica = 5
    if deska[vrstica][stolpec] == 0:
        return vrstica
    else:
        while deska[vrstica][stolpec] != 0:
            vrstica -= 1
        return vrstica

#ustvarimo funkcije; vsaka preveridrug način mozne zmage

def vodoravna_zmaga(deska, zeton):
    for s in range(STEVILO_STOLPCEV - 3):
        for v in range(STEVILO_VRSTIC):
            if deska[v][s] == zeton and deska[v][s + 1] == zeton and deska[v][s+ 2] == zeton and deska[v][s + 3] == zeton:
                return True

def navpicna_zmaga(deska, zeton):
    for s in range(STEVILO_STOLPCEV):
        for v in range(STEVILO_VRSTIC - 3):
            if deska[v][s] == zeton and deska[v + 1][s] == zeton and deska[v + 2][s] == zeton and deska[v + 3][s] == zeton:
                return True

def pozitivna_diagonalna_zmaga(deska, zeton):
    for s in range(STEVILO_STOLPCEV - 3):
        for v in range(STEVILO_VRSTIC - 3):
            if deska[v][s] == zeton and deska[v + 1][s + 1] == zeton and deska[v + 2][s + 2] == zeton and deska[v + 3][s + 3] == zeton:
                return True

def negativna_diagonalna_zmaga(deska, zeton):
    for s in range(STEVILO_STOLPCEV - 3):
        for v in range(3, STEVILO_VRSTIC):
            if deska[v][s] == zeton and deska[v - 1][s + 1] == zeton and deska[v - 2][s + 2] == zeton and deska[v - 3][s + 3] == zeton:
                return True







#T-VMESNIK

#z uporabo numpy, ustvarimo desko v obliki matrike
def ustvari_desko():
    deska = np.zeros((6,7))
    return deska

deska = ustvari_desko()
print(deska)


#Začetni izpis igre
zacni_igro = int(input('Pritisni 1 za začetek igre:'))

print('Enter 1')

#definirjamo zmago; nastavimo konec_igre na true takrat ko je ena od moznih vrst vzpostavljena
def zmagaj(deska, zeton):
    konec_igre = False
    if vodoravna_zmaga(deska,zeton) == True:
        print('Bravo Igralec ' + str(zeton) + ' zmagal oz. zmagala si!')
        konec_igre = True
    elif navpicna_zmaga(deska, zeton) == True:
        print('Bravo Igralec ' + str(zeton) + ' zmagal oz. zmagala si!')
        konec_igre = True
    elif pozitivna_diagonalna_zmaga(deska, zeton) == True:
        print('Bravo Igralec ' + str(zeton) + ' zmagal oz.zmagala si!')
        konec_igre = True
    elif negativna_diagonalna_zmaga(deska, zeton) == True:
        print('Bravo Igralec ' + str(zeton) + ' zmagal oz. zmagala si!')
        konec_igre = True
    if konec_igre:
        os._exit(1)
    else:
        pass

if zacni_igro == 1:
    print(deska)
    print('Igralec 1 tvoj zeton je' + ' ' + str(zeton_igralca_1))
    print('Igralec 2 tvoj zeton je' + ' ' + str(zeton_igralca_2))
    while not konec_igre:
        #prvi igralec na potezi
        #preveri vsako potezo za zmago
        if POTEZA % 2 == 0:
            stolpec = int(input('Igralec 1 izberi stolpec: '))
            while (stolpec) > 6 or (stolpec) < 0:
                print('Izbrati moraš med 0 in 6, duh')
                stolpec = int(input('Igralec 1 izberi stolpec: '))
            while dovoljena_poteza(deska, stolpec) != True:
                print('a ne vids da sm nemors dt, se enkrat le pls')
                stolpec = int(input('Igralec 1 izberi stolpec: ' ))
                while (stolpec) > 6 or (stolpec) < 0:
                    print('Izbrati moraš med 0 in 6, duh')
                    stolpec = int(input('Igralec 1 izberi stolpec: '))
            if dovoljena_poteza(deska, stolpec) == True:
                vrstica = prva_prazna_vrstica(deska, stolpec)
                igralna_poteza(deska, vrstica, stolpec, zeton_igralca_1)
            zmagaj(deska, zeton_igralca_1)
        #enako za drugega igralca
        
        else:
            stolpec = int(input('Igralec 2 izberi stolpec: '))
            while (stolpec) > 6 or (stolpec) < 0:
                print('Izbrati moraš med 0 in 6, duh')
                stolpec = int(input('Igralec 2 izberi stolpec: '))
            while dovoljena_poteza(deska, stolpec) != True:
                print('a ne vids da sm nemors dt, se enkrat le pls')
                stolpec = int(input('Igralec 2 izberi stolpec: '))
                while (stolpec) > 6 or (stolpec) < 0:
                    print('Izbrati moraš med 0 in 6, duh')
                    stolpec = int(input('Igralec 1 izberi stolpec: '))
            if dovoljena_poteza(deska,stolpec) == True:
                vrstica = prva_prazna_vrstica(deska, stolpec)
                igralna_poteza(deska,vrstica, stolpec, zeton_igralca_2)
            zmagaj(deska, zeton_igralca_2)
        
        POTEZA += 1
        print(deska)

