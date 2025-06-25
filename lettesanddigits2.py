s=input()
letters=""
digits=""
for i in s:
    if i.isalpha():
        letters = letters+i
    elif i.isdigit():
        digits=digits+i
sumdigits=0
for k in digits:
    sumdigits=int(k)+sumdigits
newchar=letters+str(sumdigits)
print(newchar)