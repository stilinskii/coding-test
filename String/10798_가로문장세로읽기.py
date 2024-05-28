lines = []
# 5줄 input받기
for i in range(5):
    lines.append(input()) 
#5개 문장중에서 제일 긴 것의 수 찾기
cnt = max(len(lines[0]),len(lines[1]),len(lines[2]),len(lines[3]),len(lines[4]))
string_to_return=""
#제일 긴 문장만큼 반복문돌려서 문장당 글자 하나씩 순서대로 출력
for i in range(cnt):
    for line in lines:
        if(len(line) > i):
            string_to_return += line[i]
            
print(string_to_return)