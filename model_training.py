"""Przygotowanie danych do trenowania modelu Machine Learning."""


def prepare_training_data(values: list[float]) -> list[float]:
    """Normalizuje wartości przez podzielenie ich przez maksimum."""
    if not values:
        return []

    maximum = max(values)

    if maximum == 0:
        return [0.0 for _ in values]

    return [value / maximum for value in values]


if __name__ == "__main__":
    customer_spending = [350, 1200, 7500, 850, 3200, 9800]

    normalized_data = prepare_training_data(customer_spending)

    print("Dane przygotowane do trenowania modelu:")
    print(normalized_data)
