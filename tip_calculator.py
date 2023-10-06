# Name : ODEGI CHRISTINE
# Reg no : SCT211-0093/2022

bill = int(input("Enter bill: "))
customers = int(input("Enter number of people splitting the bill: "))

def tip_amount(amount : int):
    if amount <= 2000:
        tip = amount * 0.01

    elif amount <= 7000:
        tip = amount * 0.12

    elif amount > 7000:
        tip = amount * 0.15

    return tip

amount_to_tip = tip_amount(bill)
total_bill = bill + amount_to_tip

split_bill = total_bill/customers
rounded_bill = round(split_bill, 2)

print(f"Bill to be paid by each person = {rounded_bill}")