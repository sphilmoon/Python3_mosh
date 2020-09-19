temperature = 31

if temperature > 30: # greater than 30 degree
    print("It's a hot day")
else:
    print("It's not a hot day")


username = "sphilmoon"

if len(username) <= 5: # first if condition # the length of index.
    print("your username must be at least 5 characters")
elif len(username) > 50: # second if condition
    print("your username must be less than 50 characters")
else: # aka otherwise, anything between 5-50 characters.
    print("your username looks good!")
