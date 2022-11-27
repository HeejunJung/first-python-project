#반복문 -> 유지보수가 편해졌다, 중복되는 코드르 로직으로 풀어냈을 때의 효과
i = 10
while True:
    i = i - 1
    print(i)
    if i < 1 :
        print("끝")
        break;

k = 10
while k > -1:
    print(k)
    k = k -1
print("끝"+str(k))
    