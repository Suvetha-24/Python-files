s = input("Enter string: ").strip()
count = 1
spam = False

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
        if count == 3:
            spam = True
            break
    else:
        count = 1

if spam:
    print("Spam")
else:
    print("Safe")
