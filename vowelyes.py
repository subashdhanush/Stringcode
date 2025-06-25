
userInput = input()
vowels="aeiou"
has_vowel=False
for i in userInput:
    if i.lower() in vowels:
        has_vowel=True
if has_vowel:
    print("yes")
else:
    print("no")
        