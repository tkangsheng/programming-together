import re

x = 'From: using the : character'

first_match = 'From:'
second_match = 'From: using the :'
result = re.findall('F.+:', x)
print(result)