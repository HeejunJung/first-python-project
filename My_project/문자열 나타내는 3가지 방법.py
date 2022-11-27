#구구단 만들기

#string 출력
for a in range(2,10):
    for b in range(1,10):
        matrix = '%d x %d = %d' % (a, b, a*b)
        print(matrix)

#str.format
for a in range(2,10):
    for b in range(1,10):
        print("{0} x {1} = {2}".format(a, b, a*b))

#f-string
for a in range(2,10):
    for b in range(1,10):
        print(f"{a} x {b} = {a*b}")