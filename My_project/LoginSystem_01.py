in_id = input("네이버 이메일을 입력해주세요: ") #input은 프로그램 실행을 Enter을 누를 때 까지 대기
in_password = input("비밀번호를 입력해주세요 초기 비밀번호는 생년월일입니다.ex)5월1일->0501: ")
id_jung = "young07m@naver.com"
id_kim = "0901pad@naver.com"
password_jung = "0627"
password_kim = "0901"

if in_id == id_jung and in_password == password_jung:
    print(id_jung.upper()) #upper()->값을 대문자로 바꿔줌
    print("정희준님 안녕하세요!!")
elif in_id == id_kim and in_password == password_kim:
    print("김가현님 안녕하세요!!")
else:
    print("아이디/비밀번호를 잘못입력하셨습니다.")