data = [1,2,3,4,5,6,7,8,9,10,11]
# 기존 방식
n = len(data)
if n>10:
    print(f"데이터가 너무 큽니다 ({n}개)")

# walrus operator 활용
if(n := len(data)) > 10:
    print(f"데이터가 너무 큽니다 ({n}개)")