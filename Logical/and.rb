#저장된 키값
real_id = "young07m"
real_pwd = "0627hj"

#로그인
print("아이디와 비밀번호를 입력해주세요: ")
in_id, in_pwd = gets.chomp().split() #값 입력받기

if real_id == in_id and real_pwd == in_pwd
    puts("Hello!")  
else
    puts("저장된 정보가 없습니다.")
end