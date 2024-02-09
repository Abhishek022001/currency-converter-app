from forex_python.converter import CurrencyRates

class CurrencyConverter:
 def __init__(self):
  self.currency_rates = CurrencyRates()

 def convert_currency(self, amount, from_currency, to_currency):
  try:
     exchange_rate = self.currency_rates.get_rate(from_currency, to_currency)
     converted_amount = amount * exchange_rate
     print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
  except Exception as e:
     print(f"Error: {e}")

# Example usage

currency_converter = CurrencyConverter()

# To get user input for conversion

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency (e.g., USD): ").upper()
to_currency = input("Enter the target currency (e.g., EUR): ").upper()

# Convert the currencies based on user input

currency_converter.convert_currency(amount, from_currency, to_currency)
