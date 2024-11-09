from test.currency_api import get_exchange_rates
from test.currency_converter import convert


def main():
    exchange_rates = get_exchange_rates()
    if not exchange_rates:
        return

    print("Добро пожаловать в программу обмена валют!")
    print("Доступные валюты:", ", ".join(exchange_rates.keys()))

    from_currency = input("Введите валюту, которую вы хотите обменять (например, RUB, USD): ").upper()
    to_currency = input("Введите валюту, которую вы хотите получить: ").upper()

    if from_currency == to_currency:
        print("Валюты совпадают. Обмен невозможен.")
        return

    try:
        amount = float(input(f"Введите сумму в {from_currency}: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            return
    except ValueError:
        print("Некорректный ввод суммы.")
        return

    converted_amount = convert(amount, from_currency, to_currency, exchange_rates)

    if converted_amount is not None:
        print(f"{amount} {from_currency} -> {converted_amount} {to_currency}")


if __name__ == "__main__":
    main()
