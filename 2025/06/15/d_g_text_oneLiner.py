# 문자열 처리 원 라이너
text = "Hello World Python Programming"
word_length = {word: len(word) for word in text.split()}
vowel_count = sum(1 for char in text.lower() if char in 'aeiou')

print(f"word_length: {word_length}")
print(f"vowel_count: {vowel_count}")