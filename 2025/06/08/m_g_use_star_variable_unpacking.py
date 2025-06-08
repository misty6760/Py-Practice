# *을 이용한 가변 언패킹
numbers = [1,2,3,4,5]
a, *b = numbers
print(a)            # 출력: 1
print(b)            # 출력: [2,3,4,5]
print("-----------------------------")

*a ,b = numbers
print(a)            # 출력: [1,2,3,4]
print(b)            # 출력: 5
print("-----------------------------")

a, *b, c = numbers
print(a)            # 출력: 1
print(b)            # 출력: [2,3,4]
print(c)            # 출력: 5