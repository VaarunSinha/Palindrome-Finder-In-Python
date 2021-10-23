# Number
print("Palinderome number finder!")

# Input
Number = input("Enter your number: ")
try:
    int(Number)
except ValueError:
    print("Please Enter a Number")
    Number = input("Enter your number: ")

# Reverse
Reversed_Num = Number[::-1]
# Check if it's a palindrome Number.
if int(Reversed_Num) == int(Number):
    print("{} is a palindrome number 😊".format(Number))
else:
    print("{} is not a palindrome number 🤨".format(Number))

# Word

print("Palindrome Word finder!")

# Input
String = input("Enter your word: ")
# Reverse
Reversed_String = String[::-1]
# Check if it's a palindrome word.
if Reversed_String == String:
    print("{} is a palindrome word 😊".format(String))
else:
    print("{} is not a palindrome word 🤨".format(String))
