# 리스트 연산
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))

print(f"squared: {squared}")
print(f"filtered: {filtered}")