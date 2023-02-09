a, b = map(int, input().split(" "))
multi_a = a
multi_b = b
while multi_a != multi_b:
    if multi_a > multi_b:
        multi_b += b
    else:
        multi_a += a
print(multi_a)
