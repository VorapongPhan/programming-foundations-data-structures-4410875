def has_unique_characters(data):
    set_data = frozenset(list(data))
    return len(set_data) == len(data)
  
print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
