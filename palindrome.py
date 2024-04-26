
# anagram checker

# wordInput = "racecar"
wordInput = "racecal"

letterList = list(wordInput)

# use list(reversed(x)) to reverse a list. reverse() changes things in place for rest of program
reverseLetterList = list(reversed(letterList))

if(letterList == reverseLetterList):
    print("Word input is a palindrome")
else:
    print("Word input is not a palindrome")

print("Meow")
print(letterList)
print(reverseLetterList)

