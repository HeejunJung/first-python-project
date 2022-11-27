#사용자 계정 생성
create_name = input("사용하실 이름/닉네임을 입력해주세요: ") 
create_id_ID = input("통합이메일시스템에 오신 것을 환영합니다. 사용하실 아이디를 입력해주세요 ex)young07m@naver.com -> young07m: ")
while True:
        create_id_mailaddress = input("기존사용중이신 사이트를 입력해주세요.\n1.naver.com\n2.google.com\n3.daum.net\n4.직접입력(.com형식)\n선택:  ")
        if create_id_mailaddress == "1" or create_id_mailaddress == "1." or create_id_mailaddress == "naver" or create_id_mailaddress == "naver.com":
            create_id = create_id_ID + "@naver.com"
            break;
        elif create_id_mailaddress == "2" or create_id_mailaddress == "2." or create_id_mailaddress == "google" or create_id_mailaddress == "google.com":
            create_id = create_id_ID + "@google.com"
            break;
        elif create_id_mailaddress == "3" or create_id_mailaddress == "3." or create_id_mailaddress == "daum" or create_id_mailaddress == "daum.net":
            create_id = create_id_ID + "@daum.net"
            break;
        else:
            if ".com" in create_id_mailaddress:
                print("확인되었습니다.")
                create_id = create_id_ID + "@" +create_id_mailaddress
                break;
        print("맞지않는 이메일 형식입니다.")

#비밀번호 확인 시스템
create_password = input("사용하실 비밀번호를 입력해주세요: ") 
while True:
    check_password = input("비밀번호를 한 번 더 입력해주세요: ")
    if check_password == create_password:
        print("저장중.....\n확인되었습니다. 로그인 창으로 이동합니다.")
        id_user = create_id  #서버에 저장하기
        password_user = create_password #서버에 저장하기
        break;
    print("오류입니다.")

#로그인하기
print("---------------로그인창---------------")
while True:
    in_id = input("이메일을 입력해주세요: ")
    in_password = input("비밀번호를 입력해주세요: ")
    if in_id == id_user and in_password == password_user:
        print(create_name + "님 통합메일시스템에 오신 것을 환영합니다.")
        break;
    print("아이디/비밀번호를 잘못입력하셨습니다.")

