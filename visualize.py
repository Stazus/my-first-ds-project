
"""Wizualizacja wydatkow klientow przy uzyciu matplotlib."""

import matplotlib.pyplot as plt


def plot_customer_spending(
    customers: list[str],
    spending: list[float],
) -> None:
    """Tworzy wykres slupkowy wydatkow klientow."""
    if len(customers) != len(spending):
        raise ValueError("Liczba klientow i wydatkow musi byc taka sama.")

    if not customers:
        raise ValueError("Lista klientow nie moze byc pusta.")

    plt.figure(figsize=(10, 6))
    plt.bar(customers, spending, color="steelblue")

    plt.title("Wydatki klientow")
    plt.xlabel("Klienci")
    plt.ylabel("Wydatki (PLN)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig("customer_spending.png")
    plt.close()

    print("Wykres zapisano w pliku customer_spending.png")


if __name__ == "__main__":
    customers = [
        "Klient 1",
        "Klient 2",
        "Klient 3",
        "Klient 4",
        "Klient 5",
        "Klient 6",
    ]

    spending = [350, 1200, 7500, 850, 3200, 9800]

    plot_customer_spending(customers, spending)
