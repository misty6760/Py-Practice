# 제너레이터 표현식: 0부터 9까지 제곱수 생성
squares = (x**2 for x in range(10))

# 0부터 9까지의 재곱수 출력
for square in squares:
    print(square, end=" ")