def describe_person(person):
    match person:
        case {"name": name, "age": age, "address": {"city": city}}:
            return f"{name}는 {city}에서 살고 있으며 나이는 {age}입니다."
        case {"name": name, "age": age}:
            return f"{name}의 나이는 {age}입니다."
        case _:
            return "알 수 없음."

person1 = {"name": "김철수", "age": 21}
person2 = {"name": "김영희", "age": 23, "address": {"city": "서울"}}
print(describe_person(person1))
print(describe_person(person2))