n = int(input())
count = 1
i = 0

for j in range(1, n+1):
    if j == (6*(count-1))+(6*count)+1:
        count += 1

print(count)
