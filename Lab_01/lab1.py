def apply_discount(prices, percent):
    # Перевірка на адекватність знижки
    if percent < 0 or percent > 100:
        raise ValueError("Знижка має бути від 0 до 100")

    # Рахуємо нові ціни і округлюємо до 2 знаків
    discounted = []
    for price in prices:
        new_price = price * (1 - percent / 100)
        discounted.append(round(new_price, 2))
        
    return discounted


def transform_all(values, func):
    # Застосовуємо передану функцію до кожного елемента
    result = []
    for v in values:
        result.append(func(v))
    return result


def calculate_total(prices):
    # Сума
    return sum(prices)


def main():
    prices = [100.00, 59.90, 40.00]
    
    discounted_prices = apply_discount(prices, 15)
    
    print("Ціни зі знижкою:", discounted_prices)
    print("Загальна сума:", calculate_total(discounted_prices))
    
    # Використання простої лямбди
    print("Квадрати чисел:", transform_all([1, 2, 3], lambda x: x ** 2))


if __name__ == "__main__":
    main()
