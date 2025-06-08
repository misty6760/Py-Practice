# 기본 리스트
my_list = [10, 20, 30, 40, 50]

# 리스트의 이터레이터 객체 생성
list_iter = iter(my_list)

# next()를 사용하여 값 순차적으로 가져오기
print(next(list_iter))          # 10
print(next(list_iter))          # 20
print(next(list_iter))          # 30
print(next(list_iter))          # 40
print(next(list_iter))          # 50

#더이상 값이 없으면 StopIteration 예외가 발생
# print(next(list_iter))        # StopIteration 예외 발생

print("------------------")

# for문을 사요앟여 리스트 값 출력
for itme in my_list:
    print(itme)