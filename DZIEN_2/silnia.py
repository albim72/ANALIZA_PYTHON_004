#n! = 1*2*...*n!
import sys
import pandas as pd
import xlsxwriter

#sys.set_int_max_str_digits(0x1000000)
def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    wynik =1
    for i in range(1,n+1):
        wynik *= i

    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    wynik = {"n":n,
             "wynik dzielenia silnia":silnia(n)/silnia(n-3)
             }
    print(f"silnia dla n = {n} wynosi {wynik}")
    df = pd.DataFrame(wynik)
    writer = pd.ExcelWriter('silnia.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='factorial')
    writer.save()
except ValueError as ve:
    print(ve)
