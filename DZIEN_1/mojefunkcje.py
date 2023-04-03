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
