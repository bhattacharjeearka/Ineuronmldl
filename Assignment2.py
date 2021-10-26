# Problem 1
row = 5
symbol = '*'

for i in range(0, row, 1):
    for j in range(0, i+1):
        print(symbol, end=' ')
    print(" ")

for i in range(row, 0, -1):
    for j in range(0, i-1):
        print(symbol, end=' ')
    print(" ")


# Problem 2

Word = str(input("Enter a word: "))
print(Word[::-1])
