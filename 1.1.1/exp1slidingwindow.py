def plus_one_sliding_window(digits):
    carry = 1
    left = len(digits) - 1
    right = len(digits) - 1

    while left >= 0:
        total = digits[right] + carry
        digits[right] = total % 10
        carry = total // 10

        left -= 1
        right -= 1

    if carry:
        digits.insert(0, carry)

    return digits


arr = list(map(int, input("Enter the digits: ").split()))
print(plus_one_sliding_window(arr))