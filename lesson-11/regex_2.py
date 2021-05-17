import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
sample = '123 456 winston takes a walk'
regex_pattern = '[a-z][a-z\s]+[a-z]'

print(re.findall(regex_pattern, sample))