# 조건부 딕셔너리 생성
user_data = {'name': 'John', 'age': None, 'email': 'john@example.com'}
clean_data = {k: v for k, v in user_data.items() if v is not None}

print(f'clean_data: {clean_data}')