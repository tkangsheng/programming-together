# Summary

To recap the things we learned today:

# Contents
- [Summary](#summary)
- [Contents](#contents)
  - [1. Operator precedence](#1-operator-precedence)
  - [2. Variable types](#2-variable-types)
  - [3. Getting user inputs (prompts in terminal(mac) or powershell/command-prompt (windows))](#3-getting-user-inputs-prompts-in-terminalmac-or-powershellcommand-prompt-windows)
  - [4. Comments](#4-comments)
  - [5. If condition](#5-if-condition)
  - [6. Indentation defines scope](#6-indentation-defines-scope)
  - [7. Spacebar whitespace shld be used instead of tab whitespace](#7-spacebar-whitespace-shld-be-used-instead-of-tab-whitespace)
  - [8. Try except](#8-try-except)

## 1. Operator precedence
1) parentheses (expressions in brackets get evaluated first)
2) exponentiation (2 ** 3 == 8)
3) multiplication, division, modulo (213/7%4 == 63/7 % 4 == 9 % 4 == 1)
4) addition, subtraction
5) left to right

## 2. Variable types

- type conversion
- type strictness
- division of integers produces float (10/5 == 2.0)

## 3. Getting user inputs (prompts in terminal(mac) or powershell/command-prompt (windows))

- x = input('tell me a number') # x will be a string of what the user typed

## 4. Comments

```python
    # this is a comment in python code
```

## 5. If condition

- if, elif, else
- comparison operators `(a < b or a <= b or a == b or a >= b or a > b or a != b)`
- indentation

## 6. Indentation defines scope

Given some code:

-------------------------------------------

```python
conditionIsMet = True
x = 4
if conditionIsMet:
    doSomething()
    x = 7
else
    doSomethingElse()
x = 8
```

-------------------------------------------
Is x equal to 7 or 8 or 4? (ans: 8)

## 7. Spacebar whitespace shld be used instead of tab whitespace

## 8. Try except

`try` block is attempted by python then if some exception occurs (Traceback) then python will stop wherever the code failed in the `try` block and jump to the `except` block of code will run.

```python
   try:
        print('try to do something')
   except:
        print('do something when an exception occurred in the try block')
```
