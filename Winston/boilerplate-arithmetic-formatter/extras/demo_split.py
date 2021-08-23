
sentence = "32    +8"

index_of_operator = sentence.find('+')
result = sentence[0:index_of_operator]
result = result.strip()

print(result)
