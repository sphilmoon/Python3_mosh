names = ['Phil', 'Bob', 'Katie', 'John', 'Sam']
print(names[0:3]) # excluding John and Sam

# Finding the largest number on the list:
# If in for loops:
numbers = [12, 24, 6, 2, 8, 4, 10]
max = numbers[0] # defining a max varible from the numbers variable.
# starting with 0th index in the for loop below, but it really
# doesn't matter which index to start with.
for number in numbers:
    if number > max:
        max = number # setting a new max.
print(max)
