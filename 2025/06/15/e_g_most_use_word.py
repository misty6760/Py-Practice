# s = "mississippi"
# most_used = [max(set(s), key=lambda word: s.count(word))]
#
# print(most_used)

s = "mississippi"

max_char = max(set(s), key=lambda x: s.count(x))
max_count = s.count(max_char)

result = [char for char in set(s) if s.count(char) == max_count]

for char in result:
    print(char)
