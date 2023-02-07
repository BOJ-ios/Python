N = int(input())
if N == 1:
    print("1")
else:
    _min, _max, count = [2, 7, 2]
    while True:
        if _min <= N and N <= _max:
            print(count)
            break
        else:
            _min += 6 * (count - 1)
            _max += 6 * count
            count += 1
