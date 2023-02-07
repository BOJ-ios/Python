a = int(input())
result = a
while (a > 0):
    result += a % 10
    a = a // 10
print(result)
