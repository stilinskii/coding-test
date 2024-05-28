# 왜 ㄱㅖ속 runtime error가 나는지 모르겠음
cnt = int(input()) #입력받을 문장 개수 
words = []
for i in range(cnt):
    words.append(input()) #문장 입력받음
    
for word in words:
    dictionary = dict() #문장의 한 글자씩 키로 해서 같은 값이 얼마나 나왔는지 값에 저장
    for char in word:
        if char != " ":
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    
    sorted_dictionary = sorted(dictionary.values(),reverse=True) # 값을 리스트로 불러와서 desc
    if(sorted_dictionary[0] == sorted_dictionary[1]): #제일 큰 값이 2개 있으면 "?"" 출력
        print("?")
    else:
        for key in dictionary.keys(): 
            if dictionary[key] == sorted_dictionary[0]: #제일 큰 값을 가진 key 출력
                print(key)
                break
            
    