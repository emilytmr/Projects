number = int(input("Write a number:"))

multiply = 1

for calc in range(1, number + 1):
    print(calc)
    multiply *= calc

print(multiply)