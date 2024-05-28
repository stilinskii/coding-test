#문장 몇개 입력받을건지 입력받기
cnt = int(input())
#앞 뒤에 뭐 와야하는지 *로 구분해서 받기
pattern = input().split("*")
# 한곳에서만 쓰는게 아니기 때문에 틀릴 수 있어서 변수에 저장
yes = "DA"
no = "NE"

for i in range(cnt):
    name= input()
    #패턴 앞뒤보다 짧으면 이미 아니기때문에 no 출력
    if len(name) < len(pattern[0])+len(pattern[1]):
        print(no)
        continue
    #입력값의 처음부터 패턴의 길이만큼의 글자가 패턴 앞부분과 같거나 
    # 입력값의 뒤에서 패턴 뒷부분 길이만큼의 부분이 패턴의 뒷부분과 같다면 yes 출력
    if name[0:len(pattern[0])] == pattern[0] and name[-len(pattern[1]):] == pattern[1]:
        print(yes)
    else:
        # 아니면 no
        print(no)