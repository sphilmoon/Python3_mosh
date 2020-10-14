# dictionary is for unordered set of key/value pairs. 

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birth"] = "jan 1 2002"
print(customer["birth"])

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)
