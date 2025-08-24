import requests

def get_exchange_rate(src, tgt):
    """
    Fetch latest exchange rate from exchangerate.host
    """
    url = f"https://api.exchangerate.host/convert?from={src}&to={tgt}"
    try:
        response = requests.get(url)
        data = response.json()
        if data and data['info'] and 'rate' in data['info']:
            return data['info']['rate']
        else:
            print("Error: Could not get exchange rate.")
            return None
    except Exception as e:
        print(f"API error: {e}")
        return None

def currency_converter():
    print("=== Currency Converter ===")
    amount_str = input("Enter amount: ").strip()
    if not amount_str.replace('.', '', 1).isdigit():
        print("Invalid amount.")
        return
    amount = float(amount_str)
    src = input("From currency (e.g. USD): ").strip().upper()
    tgt = input("To currency (e.g. INR): ").strip().upper()

    rate = get_exchange_rate(src, tgt)
    if rate is not None:
        converted = amount * rate
        print(f"\n{amount:.2f} {src} = {converted:.2f} {tgt}")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    currency_converter()
