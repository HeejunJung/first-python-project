#저장된 키값
real_egoing = "egoings"  
real_k8805 = "k8805"

#로그인
while True:
    in_key = input("키값을 입력해주세요: ") #문자열
    if real_egoing == in_key or real_k8805 == in_key:
        print("Hello!")
        break;
    print("등록된 정보가 없습니다.")