file = open('lesson-10\words.txt')

word_histogram = dict()

for line in file:
    line = line.replace('.', ' ')
    line = line.replace(',', ' ')
    words_in_line = line.split()
    for word in words_in_line:
        word_histogram[word] = word_histogram.get(word, 0) + 1

value_key_list = sorted(
    [ (value, key) for key,value in word_histogram.items() ],
    reverse=True
)

for value, key in (value_key_list[:10]):
    print(key, value)
