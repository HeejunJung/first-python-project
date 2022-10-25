#문자의 표현
from gettext import find
from multiprocessing.pool import ApplyResult
from tkinter import E
from turtle import right
from winreg import HKEY_LOCAL_MACHINE

print('Hello') #작은 따옴표
print("Hello") #큰 따옴표
print("Hello 'hello'") #'출력하기
print('Hello "hello"')

#문자열의 제어
print('Hello ' + 'world') #문자열 더하기
print('Hello ' * 3) #문자열 곱하기
print('Hello' [0]) #문자열 중 하나만 골라서 출력하기
print('Hello' [1])

#문자열의 제어2
print('hello world'.capitalize()) #첫글자 대문자
print('hello world'.upper()) #모든 글자 대문자 
print('Hello world'.__len__()) #문자열 길이 측정1
print(len('Hello world')) #문자열 길이측정2
print('Hello world'.replace('world', 'programming')) #원하는 문자열 바꾸기
#print('Hello world'.replace('Hello', 'Heejun'))

#특수문자
print("egoing's \"tutorial\"") #\->escpae
print("\\") #\출력하기
print("Hello\nworld") #줄바꿈, n=new line
print("Hello\tworld") #tab키
print("\a")
print('Hello\tworld') #작은 따옴표, 큰 따옴표 처리 같음

#문자와 숫자 데이터 타입
print(10+5)
print("10" + "5")
