#WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 94.53 #-----> as June 22 2026
    print("USD =" ,usd_val, "INR =" ,inr_val,)

converter(99)