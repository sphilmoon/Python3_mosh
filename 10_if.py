price = 1E6
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}") # formatted string.
