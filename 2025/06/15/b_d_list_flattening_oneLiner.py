# 리스트 플래트닝
nested_list = [[1,2], [3,4], [5,6]]
flattened = [item for sublist in nested_list for item in sublist]

print(f"flattened: {flattened}")