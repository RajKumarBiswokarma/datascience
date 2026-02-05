import mymodule


num1 = int(input("Enter First Number  "))
num2 = int(input("Enter Second Number "))


sum_of_number = mymodule.add(num1, num2)
difference = mymodule.subtract(num1, num2)

print("Sum of the Two Number are :  ", sum_of_number)
print("Differenceof number are :  ", difference)


if __name__ == "__main__":
    print("Sum of number ", mymodule.add(1, 2))
