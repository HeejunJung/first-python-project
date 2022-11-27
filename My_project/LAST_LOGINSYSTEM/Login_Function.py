 #시작질문
def question():
    Yes_No = input("HJ.com의 계정이 있으신가요?(Y/N): ")
    if Yes_No == 'Y':
        return True
    return False

#아이디/비밀번호/닉네임 생성
def make_ID(database_ID, database_nickname):
    print("회원가입페이지입니다.")
    while True:
        ID = input("사용하실 아이디를 입력해주세요: ")
        if ID not in database_ID:  #데이터베이스에서 사용중인 아이디와 중복인지 체크
            print("사용가능한 아이디입니다!")
            database_ID.append(ID)  #리스트에 추가
            break;
        print("중복된 아이디입니다.")
    while True:
        nickname = input("사용하실 닉네임을 입력해주세요: ")
        if nickname not in database_nickname:  #데이터베이스에서 사용중인 닉네임과 중복인지 체크
            print("사용가능한 닉네임입니다!")
            database_nickname.append(nickname)  #리스트에 추가
            break
        print("중복된 닉네임입니다.")
            
#비밀번호 생성
def make_pwd(database_pwd):
    while True:
        pwd = input("사용하실 비밀번호를 입력해주세요: ")
        check_pwd = input("비밀번호를 다시 한 번 입력해주세요: ")  #비밀번호 확인
        if pwd == check_pwd:
            print("저장중.....\n계정생성완료!")
            database_pwd.append(pwd)    #리스트에 추가
            break
        print("처음 입력하신 비밀번호와 일치하지 않습니다. 재입력바랍니다.")

#로그인
def Login(database_ID, database_pwd, database_nickname):
    while True:
        input_ID, input_pwd = input("아이디와 비밀번호를 입력해주세요: ").split()
        double_break = True
        triple_break = True
        quadra_break = True
        for check_ID in database_ID:
            for check_pwd in database_pwd:
                for nickname in database_nickname:
                    if check_ID == input_ID and check_pwd == input_pwd:
                        print(f"{nickname}님 환영합니다!!")
                        double_break = False
                        break   #첫 번째 for문 탈출
                if double_break == False:
                    triple_break = False    #두 번째 for문 탈출
            if triple_break == False:
                quadra_break = False
                break   #세 번째 for문 탈출
        if quadra_break == False:
            break   #무한루프 탈출
        print("아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요.")


