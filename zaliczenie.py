# Lista książek
ksiazki = [
    {"autor": f"Autor {i}", "tytul": f"Ksiazka {i}", "rok": 2000+i%20, "strony": 100+i, "ilosc": 3}
    for i in range(1, 26)
]

# Słownik przechowujący studentów i wypożyczone przez nich książki
studenci = {}

# Limity
MAKS_KSIAZEK_NA_STUDENTA = 5
MAKS_STUDENTOW = 15

# Symulowane dane wejściowe (dla środowisk bez inputu)
uzytkownik_input = iter([
    '1',  # Pokaż książki
    '2', 'Autor Testowy', 'Tytul Testowy', '2020', '300', '2',  # Dodaj książkę
    '1',  # Pokaż książki ponownie
    '5', 'Student Jeden', '0',  # Wypożycz książkę
    '6',  # Pokaż przypomnienie o zwrocie
    '7'  # Zakończ
])

# Zastępowanie input() w testach
def mock_input(prompt):
    try:
        print(prompt)
        return next(uzytkownik_input)
    except StopIteration:
        print("Brak więcej danych wejściowych.")
        exit()

# Wyświetlanie książek
def pokaz_ksiazki():
    for i, ksiazka in enumerate(ksiazki):
        print(f"{i}. {ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['rok']}), {ksiazka['strony']} stron, {ksiazka['ilosc']} dostępnych")

# Dodanie nowej książki
def dodaj_ksiazke():
    autor = mock_input("Autor: ")
    tytul = mock_input("Tytuł: ")
    rok = int(mock_input("Rok wydania: "))
    strony = int(mock_input("Liczba stron: "))
    ilosc = int(mock_input("Ilość egzemplarzy: "))
    ksiazki.append({"autor": autor, "tytul": tytul, "rok": rok, "strony": strony, "ilosc": ilosc})

# Edytowanie istniejącej książki
def edytuj_ksiazke():
    pokaz_ksiazki()
    idx = int(mock_input("Indeks książki do edycji: "))
    if 0 <= idx < len(ksiazki):
        ksiazki[idx]['autor'] = mock_input("Nowy autor: ")
        ksiazki[idx]['tytul'] = mock_input("Nowy tytuł: ")
        ksiazki[idx]['rok'] = int(mock_input("Nowy rok: "))
        ksiazki[idx]['strony'] = int(mock_input("Nowa liczba stron: "))
        ksiazki[idx]['ilosc'] = int(mock_input("Nowa liczba egzemplarzy: "))

# Usunięcie książki
def usun_ksiazke():
    pokaz_ksiazki()
    idx = int(mock_input("Indeks książki do usunięcia: "))
    if 0 <= idx < len(ksiazki):
        del ksiazki[idx]

# Wypożyczenie książki przez studenta
def wypozycz_ksiazke():
    if len(studenci) >= MAKS_STUDENTOW:
        print("Osiągnięto limit studentów.")
        return

    imie = mock_input("Imię studenta: ")
    if imie not in studenci:
        studenci[imie] = []

    if len(studenci[imie]) >= MAKS_KSIAZEK_NA_STUDENTA:
        print("Nie można wypożyczyć więcej niż 5 książek.")
        return

    pokaz_ksiazki()
    idx = int(mock_input("Indeks książki do wypożyczenia: "))
    if 0 <= idx < len(ksiazki) and ksiazki[idx]['ilosc'] > 0:
        ksiazki[idx]['ilosc'] -= 1
        studenci[imie].append(ksiazki[idx]['tytul'])
    else:
        print("Książka niedostępna.")

# Przypomnienie o konieczności zwrotu książek
def przypomnienie_zwrotu():
    print("Raport zwrotów:")
    for student, wypozyczone in studenci.items():
        if wypozyczone:
            print(f"{student} powinien zwrócić: {', '.join(wypozyczone)}")

# Menu główne programu
def main():
    while True:
        print("\n1. Pokaż książki\n2. Dodaj książkę\n3. Edytuj książkę\n4. Usuń książkę\n5. Wypożycz książkę\n6. Przypomnienie o zwrotach\n7. Zakończ")
        wybor = mock_input("Wybierz opcję: ")
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
            print("Niepoprawna opcja.")

if __name__ == "__main__":
    main()
