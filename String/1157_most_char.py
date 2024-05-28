# 문제 : 입력값에서 가장 많이 입력된 알파벳 하나 대문자로 출력
s = input()

s = s.strip()
s = s.upper()

d = dict()
# 입력값의 알파벳 하나씩 딕셔너리에 저장. 빈도수를 값으로
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

# 한글자면 그거 출력
if len(d) == 1:
    print(next(iter(d)))
# 값만 꺼내서 리스트로 만들고 내림차순 정렬
else:
    s_list=sorted(d.values(),reverse=True)

# 제일 큰 값이 똑같은게 2개면 ? 출력
    if s_list[0] == s_list[1]:
        print("?")
    else:
        # 딕셔너리에서 제일 큰 값을 value로 가지고있는 key 를 찾아서 key 출력
        for item in d:
            if d[item] == s_list[0]:
                print(item) 
                break