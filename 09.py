strings = ["apple", "banana", "avocado", "grape", "apricot"]   
filtered_strings = list(map(lambda s: s.startswith("a"), strings))
print(filtered_strings)