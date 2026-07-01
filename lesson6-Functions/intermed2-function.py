#WAF to convert USD to INR.

def val_usd(usd):
    INR = (usd*95.11) #------> as 7/1/2026
    print(INR)

usd = int(input("Enter the USD : "))


val_usd(usd)

