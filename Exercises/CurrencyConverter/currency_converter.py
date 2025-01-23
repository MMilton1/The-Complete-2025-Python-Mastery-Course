USD_TO_EUR = 0.92
USD_TO_CAD = 1.35
EUR_TO_USD = 1.09
EUR_TO_CAD = 1.47
CAD_TO_USD = 0.74
CAD_TO_EUR = 0.68

# Conversion formula amount_in_eur = amount_in_usd * USD_TO_EUR (target_amount)
while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Invalid amount")

currencies = ("USD", "EUR", "CAD")

while True:
    source_currency = input("Source currency (USD/EUR/CAD): ").upper()
    if source_currency not in currencies:
        print("Invalid currency")
    else:
        break


while True:
    target_currency = input("Target currency (USD/EUR/CAD): ").upper()
    if target_currency not in currencies:
        print("Invalid currency")
    else:
        break

# if source_currency.upper() == "USD" and target_currency.upper() == "EUR":
#     converted_amount = amount * USD_TO_EUR
#     print(f"{float(amount)} USD is equal to {float(converted_amount)} EUR")
# elif source_currency.upper() == "USD" and target_currency.upper() == "CAD":
#     converted_amount = amount * USD_TO_CAD
#     print(f"{float(amount)} USD is equal to {float(converted_amount)} CAD")
# elif source_currency.upper() == "EUR" and target_currency.upper() == "USD":
#     converted_amount = amount * EUR_TO_USD
#     print(f"{float(amount)} EUR is equal to {float(converted_amount)} USD")
# elif source_currency.upper() == "EUR" and target_currency.upper() == "CAD":
#     converted_amount = amount * EUR_TO_CAD
#     print(f"{float(amount)} EUR is equal to {float(converted_amount)} CAD")
# elif source_currency.upper() == "CAD" and target_currency.upper() == "USD":
#     converted_amount = amount * CAD_TO_USD
#     print(f"{float(amount)} CAD is equal to {float(converted_amount)} USD")
# elif source_currency.upper() == "CAD" and target_currency.upper() == "EUR":
#     converted_amount = amount * CAD_TO_EUR
#     print(f"{float(amount)} CAD is equal to {float(converted_amount)} EUR")
# else:
# print("Unable to complete currency conversion")


exchange_rates = {
    "USD": {"EUR": USD_TO_EUR, "CAD": USD_TO_CAD},
    "EUR": {"USD": EUR_TO_USD, "CAD": EUR_TO_CAD},
    "CAD": {"USD": CAD_TO_USD, "EUR": CAD_TO_EUR},
}


if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * exchange_rates[source_currency][target_currency]
print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")
