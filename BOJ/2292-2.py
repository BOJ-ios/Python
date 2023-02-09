n = int(input())
count = 2
i = 0

if n == 1:
    print(1)
else:
    for j in range(1, n+1):
        if j == (6*(count-2))+(6*count-1)+1 or j == (6*(count-1))+(6*count)+1:
            count += 1
    print(count)
