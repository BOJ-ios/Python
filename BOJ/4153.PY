answer = str()
while 1:
    length = sorted(list(map(int, input().split())))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    else:
        if pow(length[0], 2) + pow(length[1], 2) == pow(length[2], 2):
            answer += 'right\n'
        else:
            answer += 'wrong\n'
print(answer, end='')
