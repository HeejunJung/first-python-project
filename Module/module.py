import sub_module #전체 다 불러오기
# from sub_module import a #일부분만  불러오기
# from sub_module import a as z#이름 바꾸기


def a():
    print("자동출력")
    return 'aaa'


sub_module.a()
print(a())
