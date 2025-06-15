s = "this is a test this is a only a test"
word_counts = {word: s.split().count(word) for word in set(s.split())}

print(word_counts)