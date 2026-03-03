from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
import hashlib
import hmac
import urllib.parse

app = FastAPI()

# Your PayFast details
MERCHANT_ID = "12345678"
MERCHANT_KEY = "your_merchant_key"
PASSPHRASE = "your_secret_passphrase"
ITN_URL = "https://costbyte.co.za/payfast-itn"  # Your public endpoint

@app.post("/payfast-itn", response_class=HTMLResponse)
async def payfast_itn(request: Request):
    form_data = await request.form()

    # Validate IP (PayFast security)
    client_ip = request.client.host
    if client_ip not in ["102.132.128.0/19", "197.242.128.0/18"]:  # PayFast IP ranges
        raise HTTPException(status_code=403, detail="Invalid IP")

    # Build validation string
    data = {k: v for k, v in form_data.items() if k != "signature"}
    pf_param_string = urllib.parse.urlencode(data)
    pf_param_string += f"&passphrase={PASSPHRASE}"
    calculated_signature = hashlib.md5(pf_param_string.encode()).hexdigest()

    # Check signature
    if calculated_signature != form_data.get("signature"):
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Check payment status
    if form_data.get("payment_status") == "COMPLETE":
        # Payment success – trigger download, record revenue
        transaction_id = form_data.get("pf_payment_id")
        amount = float(form_data.get("amount_gross"))
        print(f"Payment COMPLETE: R{amount} – Transaction {transaction_id}")

        # Here: Send ZIP/PDF link via email/WhatsApp
        # Record for payout split

    return "OK"  # PayFast requires "OK" response
