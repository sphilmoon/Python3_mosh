weight = int(input('Weight:  ')) # what about the floating input?
print()
unit = input("Indicate 'lbs' or 'kg': ") # any input error for sth else?
print()

if unit.lower() == 'lbs':
        converted = weight * 0.45
        print(f"You're {converted} kg.")
else:
    converted = weight / 0.45
    print(f"You're {converted} lbs.")
