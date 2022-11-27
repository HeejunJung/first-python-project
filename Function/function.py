# result = len('aaa') #내장함수
# print(result)

#우리가 직접 함수를 만들 수 없을까?
#basic
def a3():
    print('aaa')
a3()

#return
def auto_a3():
    print('before')
    return 'aaa' #aaa값 반환
    print('after') #return은 함수를 끝내기도한다.
print(auto_a3())

#return+매개변수
def advanced_auto_a3(str):
    return 'a'*3
print(advanced_auto_a3(3))

#원하는 문자 원하는 갯수만큼 출력
def real_auto(alphabet: str, num: str):
    for result in range(int(num)):
        print(f"출력값은 {alphabet}") 
        #str = '출력값은 %s' % alphabet
        #print(str)
        #print("출력값은{0}".format(alphabet))
alphabet, num = input("원하는 문자와 횟수를 입력해주세요: ").split()
real_auto(alphabet, num)

#값 입력받기
def quiz():
    sum = input("1 + 2 = ?")
    if sum == '3':
        print("정답입니다.")
    else:
        print("오답입니다.")   
quiz()

# n : 출력할 횟수
# value : 출력할 값
def print_n_string(value, n):
    for i in range(n):
        #print("{0}".format(value)) 
        print(f"{value}")

# "잘부탁드립니다"를 5회 출력한다
print_n_string("잘부탁드립니다", 5)