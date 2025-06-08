def describe_shape(shape: (int, str)):
    # 튜플 패턴 매칭
    match shape:
        case ("circle", r):
            return f"Circle radius: {r}"
        case ("square", s):
            return f"Square side: {s}"
        case ("rectangle", w,h):
            return f"Rectangle width: {w}, height: {h}"
        case _:
            return f"Unknown shape"

# 사용 예시
print(describe_shape(("circle", 5)))
print(describe_shape(("square", 4)))
print(describe_shape(("rectangle", 3, 6)))
print(describe_shape(("triangle", 3, 4)))
