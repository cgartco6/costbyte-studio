def process_weekly_payout(business_id):
    revenue = get_weekly_revenue(business_id)
    if revenue == 0:
        days_inactive = get_days_since_last_revenue(business_id)
        if days_inactive > 60:
            if not business.has_active_subscription():
                set_limited_mode(business_id)
                send_fallback_subscription_email(business.user_id, 99)
    fee = revenue * 0.20
    client_share = revenue - fee - gateway_fees
    send_manual_eft_reminder(business.bank_details, client_share, f"COSTBYTE-{business_id}-{datetime.now().strftime('%Y%m%d')}")
    credit_costbyte_account(fee)  # funds upgrades
