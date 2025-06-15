# 리스트 중복 제거 (순서 유지)
items_with_duplicate = [1,2,2,3,1,4,3]
unique_items = list(dict.fromkeys(items_with_duplicate))

print(f'unique_items: {unique_items}')