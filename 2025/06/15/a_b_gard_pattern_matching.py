def classify_number(n):
    match n:
        case n if n < 0:
            return "음수"
        case n if n == 0:
            return "영"
        case n if n > 0:
            return "양수"
        case _:
            return "알 수 없음"

print(classify_number(-1))
print(classify_number(0))
print(classify_number(1))