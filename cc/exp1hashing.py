def plus_one_hashing(digits):
    d = {}

    for i in range(len(digits)):
        d[i] = digits[i]

    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        total = d[i] + carry
        d[i] = total % 10
        carry = total // 10

    if carry:
        result = [1]
    else:
        result = []

    for i in range(len(digits)):
        result.append(d[i])

    return result


arr = list(map(int, input("Enter the digits: ").split()))
print(plus_one_hashing(arr))