USD_TO_EUR = 0.92
USD_TO_CAD = 1.35
EUR_TO_USD = 1.09
EUR_TO_CAD = 1.47
CAD_TO_USD = 0.74
CAD_TO_EUR = 0.68


def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid amount")


def get_currency(label):
    currencies = ("USD", "EUR", "CAD")
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD): ").upper()
        if currency not in currencies:
            print("Invalid currency")
        else:
            return currency


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        "USD": {"EUR": USD_TO_EUR, "CAD": USD_TO_CAD},
        "EUR": {"USD": EUR_TO_USD, "CAD": EUR_TO_CAD},
        "CAD": {"USD": CAD_TO_USD, "EUR": CAD_TO_EUR},
    }
    if source_currency == target_currency:
        return amount
    return amount * exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted_amount = convert(amount, source_currency, target_currency)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")


main()
