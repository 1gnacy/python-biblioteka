ksiazki = [
    {"autor": f"Autor {i}", "tytul": f"Ksiazka {i}", "rok": 2000+i%20, "strony": 100+i, "ilosc": 3}
    for i in range(1, 26)
]

studenci = {}

MAKS_KSIAZEK_NA_STUDENTA = 5
MAKS_STUDENTOW = 15

def pokaz_ksiazki():
    for i, ksiazka in enumerate(ksiazki):
        print(f"{i}. {ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['rok']}), {ksiazka['strony']} stron, {ksiazka['ilosc']} dostępnych")

def dodaj_ksiazke():
    autor = input("Autor: ")
    tytul = input("Tytuł: ")
    rok = int(input("Rok wydania: "))
    strony = int(input("Liczba stron: "))
    ilosc = int(input("Ilość egzemplarzy: "))
    ksiazki.append({"autor": autor, "tytul": tytul, "rok": rok, "strony": strony, "ilosc": ilosc})

def edytuj_ksiazke():
    pokaz_ksiazki()
    indeks = int(input("Podaj indeks książki do edycji: "))
    if 0 <= indeks < len(ksiazki):
        ksiazki[indeks]['autor'] = input("Nowy autor: ")
        ksiazki[indeks]['tytul'] = input("Nowy tytuł: ")
        ksiazki[indeks]['rok'] = int(input("Nowy rok: "))
        ksiazki[indeks]['strony'] = int(input("Nowa liczba stron: "))
        ksiazki[indeks]['ilosc'] = int(input("Nowa ilość egzemplarzy: "))

def usun_ksiazke():
    pokaz_ksiazki()
    indeks = int(input("Podaj indeks książki do usunięcia: "))
    if 0 <= indeks < len(ksiazki):
        del ksiazki[indeks]

def wypozycz_ksiazke():
    if len(studenci) >= MAKS_STUDENTOW:
        print("Osiągnięto limit studentów.")
        return

    imie = input("Imię studenta: ")
    if imie not in studenci:
        studenci[imie] = []

    if len(studenci[imie]) >= MAKS_KSIAZEK_NA_STUDENTA:
        print("Nie możesz wypożyczyć więcej niż 5 książek.")
        return

    pokaz_ksiazki()
    indeks = int(input("Indeks książki do wypożyczenia: "))
    if 0 <= indeks < len(ksiazki) and ksiazki[indeks]['ilosc'] > 0:
        ksiazki[indeks]['ilosc'] -= 1
        studenci[imie].append(ksiazki[indeks]['tytul'])
    else:
        print("Książka niedostępna.")

def przypomnienie_zwrotu():
    print("Raport zwrotów:")
    for student, wypozyczone in studenci.items():
        if wypozyczone:
            print(f"{student} powinien zwrócić: {', '.join(wypozyczone)}")

def menu():
    while True:
        print("\n1. Pokaż książki")
        print("2. Dodaj książkę")
        print("3. Edytuj książkę")
        print("4. Usuń książkę")
        print("5. Wypożycz książkę")
        print("6. Przypomnienie o zwrotach")
        print("7. Zakończ")
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_ksiazki()
        elif wybor == '2':
            dodaj_ksiazke()
        elif wybor == '3':
            edytuj_ksiazke()
        elif wybor == '4':
            usun_ksiazke()
        elif wybor == '5':
            wypozycz_ksiazke()
        elif wybor == '6':
            przypomnienie_zwrotu()
        elif wybor == '7':
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    menu()
1