import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch the real-time exchange rate from ExchangeRate-API
def get_exchange_rate(from_currency, to_currency):
    api_key = 'your_api_key_here'  # Replace with your actual API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data['conversion_rate']
    else:
        return None

# Function to handle currency conversion
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()
        
        # Fetch exchange rate
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        
        if exchange_rate:
            converted_amount = amount * exchange_rate
            label_result.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            label_result.config(text="Error fetching exchange rate")
    except ValueError:
        label_result.config(text="Invalid amount entered")

# Set up the main application window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# List of currency codes for the dropdowns
currency_codes = ["USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY"]

# Labels and dropdown menus for currency selection
label_from_currency = tk.Label(root, text="From Currency:")
label_from_currency.pack(pady=10)
combo_from_currency = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_from_currency.set("USD")  # Default selection
combo_from_currency.pack()

label_to_currency = tk.Label(root, text="To Currency:")
label_to_currency.pack(pady=10)
combo_to_currency = ttk.Combobox(root, values=currency_codes, state="readonly")
combo_to_currency.set("EUR")  # Default selection
combo_to_currency.pack()

# Entry widget for the amount to convert
label_amount = tk.Label(root, text="Amount:")
label_amount.pack(pady=10)
entry_amount = tk.Entry(root)
entry_amount.pack()

# Button to perform the conversion
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack(pady=20)

# Label to display the conversion result
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=20)

# Start the GUI main loop
root.mainloop()
