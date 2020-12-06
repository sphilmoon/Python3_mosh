house_price = 1E6
good_credit = False

if good_credit:
    downpayment = 0.1 * house_price
else:
    downpayment = 0.2 * house_price
message = f"My downpayment is: ${downpayment}."
print(message)