# 딕셔너리 언패킹
info = {'name': 'Alice', 'age': 18}

# 키 언패킹
a, b = info
print(a, b)

# 키와 값을 모두 언패킹 (items() 이용)
for key, value in info.items():
    print(key, value)

# 출력:
# name Alice
# age 18