#저장된 키값
real_egoing = "1"
real_k8805 = "ab"

#로그인
print("키값을 입력해주세요: ")
in_str = gets.chomp() #값 입력받기

if real_egoing == in_str or real_k8805 == in_str
    puts("Hello!")  
else
    puts("저장된 정보가 없습니다.")
end