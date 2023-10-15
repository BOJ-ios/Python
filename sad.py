# data = int(input("합계를 구할 숫자 범위를 입력하세요. "))

# odd_sum = sum(range(1, data + 1, 2))
# even_sum = sum(range(0, data + 1, 2))

# print(f"0부터 {data}까지의 홀수합은 {odd_sum} 입니다.")
# print(f"0부터 {data}까지의 짝수합은 {even_sum} 입니다.")

data = int(input("합계를 구할 숫자 범위를 입력하세요. "))+1

sum = 0
for x in range(1, data, 2):
    sum = sum + x

print("0부터 {}까지의 홀수합은 {} 입니다.".format(data-1, sum))
print("0부터 {}까지의 짝수합은 {} 입니다.".format(data-1, ((data - 1) * data // 2) - sum))
