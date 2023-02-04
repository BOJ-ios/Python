alpha = [0] * 26
word = input()

for i in word:
    if (ord(i) >= ord('A') and ord(i) <= ord('Z')):
        alpha[ord(i) - 65] += 1
    else:
        alpha[ord(i) - 97] += 1

max_count = max(alpha)
count = 0
result = ''
for i in range(0, 26):
    if (alpha[i] == max_count):
        count += 1
        result = chr(i + 65)

if (count == 1):
    print(result)
else:
    print("?")
