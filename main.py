def reverse_value(value):
 reversedValue = value[::-1]
 return reversedValue

def is_palindrome(value):
    reversedValue = reverse_value(value)
    if reversedValue == value:
        return True
    else:
         return False

userInputw = input("Enter The Value:\n")

userInput = userInputw.replace(" ", "")

isPalindrome = is_palindrome(userInput)

if isPalindrome:
    print(f"{userInputw} is equal to it's reverse {userInputw} therefore it is a palindrome.")
else:
     print(f"{userInput} is not equal to it's reverse {reverse_value(userInput)} therefore it is not a palindrome.")
