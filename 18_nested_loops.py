# for loops are to iterate strings etc.
# define with a 'loop variable'.
# nested loops are loops within the loop.
# generating quardinants.

for x in range(4): # starting the quardinants from 0.
    for y in range(3): # inner loop is completed first before the outer loop.
        print(f"({x}, {y})")

# multiplying 'x' with my loop variable.
numbers = [1, 1, 1, 1, 5]
for x_count in numbers:
    print('x' * x_count)

# nested loop.
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = '' # defining a variable with an empty string.
    for count in range(x_count): # using a range function to sequence x_count.
        output += 'x'
    print(output)
