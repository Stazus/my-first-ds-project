"""Moduł do wczytywania danych w projekcie Data Science."""

import csv


def load_data(file_path):
    """Wczytuje dane z pliku CSV i zwraca listę słowników."""
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    print("Moduł wczytywania danych jest gotowy.")
