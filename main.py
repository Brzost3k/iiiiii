class Film:
    def __init__(self):
        self._title = ""
        self._rentals = 0

    def set_title(self, title):
        if len(title) <= 20:
            self._title = title
        else:
            print("Tytuł jest za długi. Maksymalna liczba znaków to 20.")

    def get_title(self):
        return self._title

    def get_rentals(self):
        return self._rentals

    def increment_rentals(self):
        self._rentals += 1


if __name__ == "__main__":
    film = Film()
    print("Początkowy tytuł filmu:", film.get_title())
    print("Początkowa liczba wypożyczeń:", film.get_rentals())

    film.set_title("Incepcja")
    print("\nPo ustawieniu tytułu:")
    print("Tytuł filmu:", film.get_title())
    print("\nLiczba wypożyczeń:", film.get_rentals())
    print("\nPrzed inkrementacją liczba wypożyczeń:", film.get_rentals())
    film.increment_rentals()
    print("Po inkrementacji liczba wypożyczeń:", film.get_rentals())
