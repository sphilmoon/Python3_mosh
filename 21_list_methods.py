# sorting the only unique numbers:

numbers = [1,2,5,3,6,2,2,2,4]
uniques = []
for duplicates in numbers: # adding non-duplicates in the uniques variable.
    if duplicates not in uniques:
        uniques.append(duplicates)
print(uniques)
