# input받은 숫자 한 글자씩 합하기
cnt = int(input())
num = input()
num_sum = 0

for i in range(cnt):
    num_sum += int(num[i])

print(num_sum)
