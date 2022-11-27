# in_str = input("아이디를 입력해주세요: ")

# members = ['youngsu', 'jiun', 'heesung', 'heejun']

# for check in members:
#     if check == in_str:
#         print(check + "님 환영합니다.")
#         import sys
#         sys.exit() #프로그램 종료시키기
# print('Who are you?')       




input_id = input("아이디를 입력해주세요: ")

def login(id):
    members = ['youngsu', 'jiun', 'heesung', 'heejun']
    for member in members:
        if id == member:
            return True
    return False

if login(input_id):
    print(f'안녕하세요 {input_id}님')
else:
    print(f'{input_id}님 누구세요??')





#결론
#로직을 한 번 밖에 쓰지않는다->함수 사용 안 해도 된다.
#로직을 여러번 쓴다-> 함수 사용 권장