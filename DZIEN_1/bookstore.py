class Book:
    #deklaracja stanu -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()


    #zachowanie -> funkcje klasy ->metody
    def create_book(self):
        print("utworzono nową książkę!")


    def print_book(self):
        print(f"Książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł,"
              f" oprawa: {self.oprawa}")

    def rabat(self,procent):
        return self.cena*procent/100

    def setcena(self,nowacena):
        self.cena = nowacena

bk1 = Book(34,"Wiedźmin","Andrzej Sapkowski",45)
bk1.print_book()
print(f"rabat od ceny {bk1.cena} zł wynosi {bk1.rabat(13):.2f} zł")
print("ZMIANA CENY")
bk1.cena = 47.8
bk1.print_book()
print(f"rabat od ceny {bk1.cena} zł wynosi {bk1.rabat(13):.2f} zł")

bk1.setcena(55.7)
bk1.print_book()
print(f"rabat od ceny {bk1.cena} zł wynosi {bk1.rabat(13):.2f} zł")


