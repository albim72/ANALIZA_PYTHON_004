#import dane
#import dane as dn
from dane import nr_filii as filia
from dane import book as ks
from funkcje.bfunkcje import czytaj_liste, czytaj_slownik


print("__________ wyświetlenie bezpośrednie _______________")
print(filia)
print(ks)

print("__________ wyświetlenie za pomocą funkcji _______________")
print(czytaj_liste(filia))
print(czytaj_slownik(ks))
