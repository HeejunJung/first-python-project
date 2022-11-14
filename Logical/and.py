#저장된 키값
real_id = "young07m"  
real_pwd = "0627hj"

#로그인
while True:
    input_id, input_pwd = input("아이디와 비밀번호를 입력해주세요: ").split() #문자열
    if real_id == input_id and real_pwd == input_pwd:
        print("Hello!")
        break; #조건문 탈출
    question = input("등록된 정보가 없습니다. 재입력해주세요(YES/NO): ")
    if question == "YES": continue #처음으로 돌아가기
    if question == "NO":
        print("프로그램을 종료합니다.")
        break; #조건문 탈출
        