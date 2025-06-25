userInput = input()
length=len(userInput)
if length%2 == 0:
    mid1 = length // 2 - 1
    mid2 = length // 2
    new_str = userInput[:mid1] + '*' + '*' + userInput[mid2+1:]
    print(new_str)
else:
    mid = length // 2
    new_str = userInput[:mid] + '*' + userInput[mid+1:]
    print(new_str)