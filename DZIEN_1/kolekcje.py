liczby = [89,3,4,6,-2,0,12,34,56,7,8,2,3,2,3,0,9,-3,9,12,2,3]

print(liczby)
print(liczby[3])
print(liczby[2:7])
print(liczby[:5])
print(liczby[4:])
print(liczby[-3])

liczby.append(90)
print(liczby)

liczby.insert(2,100)
print(liczby)

liczby.remove(12)
print(liczby)

del liczby[10]
print(liczby)

print(sorted(liczby))
print(liczby)

liczby.sort()
print(liczby)

krotka = ("Olek","Olga","Piotr",[45.99,8,9,0.34])
print(krotka)

zbior = {"Tytus",8900,True,55.8}
print(zbior)

osoba = {
    "imie":"Olga",
    "wiek":28
}

print(osoba["imie"])
