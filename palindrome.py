user = input("Enter a string: ")
lst = list(user)

if lst == "":
    user = input("Enter a string: ")
else:
    if lst[:] == lst[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")