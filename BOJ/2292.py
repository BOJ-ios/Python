n = int(input())
count = 2
_min = 2
_max = 7

if n == 1:
    print(1)
else:
    while True:
        if _min <= n and n < _max:
            break
        else:
            _max += 6*count
            _min += 6*count-1
            count += 1

print(count)
