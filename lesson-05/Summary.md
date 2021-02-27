Summary
# Contents- [Contents](#contents)
- [Contents- Contents](#contents--contents)
- [Strings](#strings)
  - [Datatype](#datatype)
  - [Characters](#characters)
  - [Iterating Through Strings](#iterating-through-strings)
    - [For Loop](#for-loop)
    - [While Loop](#while-loop)
  - [Substrings](#substrings)
    - [Slicing strings](#slicing-strings)
    - [String Concatenation](#string-concatenation)
    - [String Interpolation](#string-interpolation)
    - [Using in as logical operator](#using-in-as-logical-operator)
    - [String Comparison](#string-comparison)
    - [String Library](#string-library)
      - [Type](#type)
      - [Functions in strings](#functions-in-strings)
      - [List of methods in strings](#list-of-methods-in-strings)

# Strings
## Datatype
Reading and converting

## Characters
Looking inside strings
A character too far
s = "some string"
len(s) == len("some string") == 11

## Iterating Through Strings
Looping through strings. Since strings are
<u><b><i>an array of characters</i></b></u>,
we can iterate through them as if we are iterating through any array.

### For Loop

```python
name = "Winston"
for character in name:
    print(character)
```

### While Loop
```python
name = "Winston"
while i < len(name):
    character = name[i]
    print(character)
    i += 1
```

## Substrings

### Slicing strings
```python
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:20]) # Python
```
```python
s = 'Monty Python'
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python
```

### String Concatenation
```python
fullName = 'winston' + 'lim'
print(fullName) # winstonlim
```
### String Interpolation
```python
firstName = 'Winston'
lastName = 'Lim'
isMale = True
gender = 'boy' if isMale else 'girl'
result = f'My name is {firstName} {lastName} and I am a {gender}'
print(result) # My name is Winston Lim and I am a boy
```

### Using in as logical operator
```python
print('n' in 'orange') # True`
```

### String Comparison
```python
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word' + word + ', comes after banana.')
else: # word == 'banana'
    print('All right, bananas.')
```

### String Library
```python
word = 'Winston'
lowerCaseWord = word.lower()
print(lowerCaseWord) # winston
```

#### Type
A type called 'str' (a code for string in python) or string (colloqial)
```python
print(type(word)) # <class 'str'>
```

#### Functions in strings
The following prints all the methods in strings.
```python
print(dir(word))
```

#### List of methods in strings
```python
str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.rstrip([chars])
str.strip([chars])
str.replace(old, new[, count])
str.lower()
str.upper()
str.count(sub[, start[, end]])
```
