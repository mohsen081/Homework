number = int (input ("Please choose a number to divide:"))

l = list (range (1, number + 1))

divdl = []

for num in l:
    if number% num == 0:
        divdl.append (num)

print (divdl)