nums = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(lambda x: x % 2 == 0, nums))
even_numbers = [n for n in nums if n%2 == 0]

print(f"numbers: {even_numbers}")