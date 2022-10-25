#문자의 표현
puts('Hello')
puts("Hello")
puts("Hello 'hello'")

#문자열의 제어
puts('Hello ' + 'world')
puts('Hello ' * 3)
puts('Hello' [0])
puts('Hello' [1])

#문자열의 제어2
puts('hello world'.capitalize()) #첫글자 대문자
puts('hello world'.upcase()) #모든 글자 대문자 
puts('Hello world'.length()) #문자열 길이측정
puts('Hello world'.sub('world', 'programming')) #원하는 문자열 바꾸기

#특수문자
puts("egoing's \" tutorial\"") #\->escpae
puts("\\") #\출력하기
puts("Hello\nworld") #줄바꿈 n=newline
puts("Hello\tworld") #tab키
puts("\a")
puts('Hello\tworld') #작은 따옴표, 큰 따옴표 처리 다름

#문자와 숫자 데이터 타입
puts(10+5)
puts("10" + "5")
