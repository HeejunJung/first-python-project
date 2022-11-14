#저장된 키값
real_egoing = "1"  
real_k8805 = "ab"

#로그인
while True:
    in_key = input("키값을 입력해주세요: ") #문자열
    if real_egoing == in_key:
        print("Hello!, egoing!")
        break;
    if real_k8805 == in_key:
        print("Hello!, k8805!")
        break;
    print("등록된 정보가 없습니다.")