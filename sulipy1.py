"""
1. Feladat
Írj egy programot, ami a felhasználótól három egész számot
számot kér be egyesével, ezeket eltárolja egy listában, 
majd a képernyőre kiírja a lista tartalmát! Ha a felhasználó 
nem számot ad meg, kapjon hibaüzenetet, és ismétlődjön meg a 
bekérés!

"""

szamok = []
while True:
    try:
    
        elsoszam = int(input("Adj meg egy számot!: "))
        masodikszam = int(input("Adj meg egy számot!: "))
        harmadikszam = int(input("Adj meg egy számot!: "))
        szamok.append(elsoszam)
        szamok.append(masodikszam)
        szamok.append(harmadikszam)
        print(f"A számok listája: {szamok}")
        break
    except ValueError as e:
        print(e)
        print("ValueError: Nem számot adtál meg!")



# osztando = 10
# while True:
#     try:
#         oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot?: "))
#         print(f"A két szám osztásának az eredménye: {osztando/oszto}")
#         break
#     except ZeroDivisionError as e:
#         print(e)
#         print("ZeroDivisionError: Nullával nem osztunk")
#     except ValueError as e:
#         print(e)
#         print("ValueError: Nem számot adtál meg")
