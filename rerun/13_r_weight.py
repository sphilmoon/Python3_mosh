weight = input('Weight: ')
unit = input("kg or lbs? ")

if unit.lower() == "lbs":
    converted = weight * 0.45
    print(f"You're {converted} kg.")
else:
    converted = weight / 0.45
    print(f"You're {converted} lbs.")