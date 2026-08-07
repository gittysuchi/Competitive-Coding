num = input("Enter a number: ")

digits = list(num)

if digits == digits[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")