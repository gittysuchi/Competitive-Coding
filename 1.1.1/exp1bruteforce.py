def plus_one(digits):
    num = 0

    for digit in digits:
        num = num * 10 + digit

    num += 1

    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10

    return result[::-1]


arr = list(map(int, input("Enter the digits: ").split()))
print(plus_one(arr))