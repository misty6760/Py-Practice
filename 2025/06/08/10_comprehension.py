# 리스트 컴프리헨션 : 0부터 9까지의 제곱수 리스트 생성
squares = [x**2 for x in range(10)]
# 딕셔너리 컴프리헨션: 0부터 4까지의 숫자와 제곱수 매핑
square_dict = {x: x**2 for x in range(5)}
# 셋 컴프리헨션: 0부터 9까지의 제곱수 집합 생성
square_set = {x**2 for x in range(10)}

print(f"list comprehension: {squares}\ndict comprehension: {square_dict}\nset comprehension: {square_set}")