s = input()

articles = {"a", "an", "the"}
words = s.split()
newwords = ""
found = False  # Flag to check if any article is found

for i in range(len(words) - 1):
    if words[i].lower() in articles:
        newwords += words[i + 1] + " "
        found = True

if found:
    print(newwords.strip())
else:
    print(-1)
