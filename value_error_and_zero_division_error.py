
osztando = 10
try:
    oszto = int(input(f"Mennyivel osszam el a {osztando}-es számot?: "))
    print(f"A két szám osztásának az eredménye: {osztando/oszto}")
except ZeroDivisionError as e:
    print(e)
    print("Nullával nem osztunk")
except ValueError as e:
    print(e)
    print("Nem számot adtál meg")
