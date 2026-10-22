def addDigits(num):
    if num == 0:
        return 0

    return 1 + (num - 1) % 9


num = int(input("Enter num: "))
print("Result:", addDigits(num))