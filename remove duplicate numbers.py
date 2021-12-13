numbers = [2 ,2 , 4 ,5, 6 , 8 , 8 ,9 , 2, 6, 2, 8 , 6 , 7 , 1, 5 ]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

