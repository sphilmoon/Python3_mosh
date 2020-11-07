# printing proper error messages by the human developer.
# using TRY and EXCEPT constructions to handle errors.

try: # defining a try block.
    age = int(input('Age: '))
    income = 120592 # inserting an arbitrary variable to avoid Zero.
    risk = income / age # inserting an arbitrary variable to avoid Zero.
    print(age)
except ZeroDivisionError: # now assigning the Zero age error message.
    print()
    print('ERROR: Age cannot be zero.')
except ValueError:
    print()
    print('ERROR: Invalid value. Type a numerical value.')
