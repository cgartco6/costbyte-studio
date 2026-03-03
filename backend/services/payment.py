import stripe
import paypalrestsdk
import requests  # for crypto (CoinGate/Coinbase)

stripe.api_key = os.getenv("STRIPE_KEY")

def process_payment(amount: float, currency: str = "ZAR"):
    # Stripe global
    charge = stripe.Charge.create(amount=int(amount * 100), currency=currency.lower())
    return charge

def process_crypto(amount: float, currency: str = "BTC"):
    # Coinbase Commerce API
    api_key = os.getenv("COINBASE_KEY")
    payload = {"price_amount": amount, "price_currency": "ZAR", "crypto_currency": currency}
    r = requests.post("https://api.commerce.coinbase.com/charges", json=payload, headers={"X-CC-Api-Key": api_key})
    return r.json()["hosted_url"]

# Payout split: Calculate 40% FNB, 20% African, etc. – manual reminders
def calculate_payout(revenue: float):
    splits = {
        "40% FNB": revenue * 0.4,
        "20% African Bank": revenue * 0.2,
        "15% AI FNB": revenue * 0.15,
        "15% Reserve FNB": revenue * 0.15,
        "10% Remain in Account": revenue * 0.1
    }
    return splits
