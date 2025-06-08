def match_sequence(seq):
    match seq:
        case [1, 2, 3]:
            return "리스트 [1,2,3]"
        case [x, *rest]:
            return f"첫 번째 값: {x}, 나머지 값들: {rest}"
        case _:
            return "다른 리스트"


print(match_sequence([1, 2, 3]))
print(match_sequence([1, 2, 3, 4, 5]))
print(match_sequence([7, 8, 9]))
