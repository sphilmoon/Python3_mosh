# loop in loop

for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')
        

######################################

numbers = [5, 2, 5, 2, 2]

for star_count in numbers:
    print('*' * star_count)
    

######################################
for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')

numbers = [1, 1, 1, 1, 5]

for star_count in numbers:
    output = ""
    for star_count in range(star_count):
        output += "*"    
    print(output)