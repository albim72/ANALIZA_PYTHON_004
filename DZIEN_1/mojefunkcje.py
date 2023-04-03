# przykład 1

#CTRL+D -> duplikacja linii/bloku
#CTRL + / -> komentowanie/odkomentowanie wielu linii kodu (zaznaczonych)
def fx(k):
    return k**5

n=100
def policz(a,b,c=4,v=10):
    global n
    n = (a+b)*v - c*n + fx(b)
    return n

print(policz(6,8,11,2))
print(policz(5.6,0.07,2,8))
print(n)

print(policz(5,7,1))
print(policz(55,8))

#przypadek 2

def rank(*lang,nrrank,**inne):
    print(f"ranking języków programowania nr {nrrank} -> 1. {lang[0]}, 2. {lang[1]}, 3. {lang[2]}")

rank("Python","Java","C#",nrrank=55)
rank("Python","C++","Java","JavaScript","C#",nrrank=88)


#przypadek 3 -> funkcje anonimowe - funkcja lambda

print((lambda d:d+99)(4))
print((lambda d,k:d+99-k)(4,3))

g = lambda a,b,c=8:(a+b)/c

print(g(4,1,2))
print(g(4,1))

def multi(n):
    return lambda a:a*n

print(multi(8)(4))

num = [67,5,12,-6,0,9,133,78,99,-45,2,7,9,88,12,34,7]

nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

def tofive(n):
    return n+5

five = list(map(tofive,num))
print(five)

kwadraty = [i**2 for i in range(1,1000001)] #list comprehension -> funkcja anonimowa jednolinijkowa
print(sum(kwadraty))

imie = "Henio"
wynikT = "Lider"
wynikN = "uczestnik"

w = wynikT if imie=="Jan" else wynikN

print(w)

#przypadek 4

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczetnik konkursu: {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",46))
