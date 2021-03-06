# Python Lists

1. Algorithms - rules/steps to (solve a problem)/execute
2. Data Structures - structure to organise data in a computer

## Contents

- [Python Lists](#python-lists)
  - [Contents](#contents)
  - [Lists](#lists)
    - [Non-Collections](#non-collections)
    - [Lists of lists](#lists-of-lists)
    - [Empty Lists](#empty-lists)
    - [For Loop](#for-loop)
    - [Indexer Of List](#indexer-of-list)
    - [Lists Are Mutable](#lists-are-mutable)
    - [Range](#range)
  - [Working With Lists](#working-with-lists)
    - [Concatenating Lists](#concatenating-lists)
    - [Slicing Lists](#slicing-lists)
    - [List Methods](#list-methods)
    - [Build List From Scratch](#build-list-from-scratch)
    - [Is Something In My List?](#is-something-in-my-list)
    - [Lists Are In Order](#lists-are-in-order)
    - [Built-in Functions And Lists](#built-in-functions-and-lists)
    - [Difference In Memory](#difference-in-memory)

## Lists

A list is a collection of items and values in 1 variable.
We can think of lists as a collection of variables.

```python
friends = [ 'Joseph', 'Glenn', 'Sally' ]
scores = [ 1, 2, 3 ]
```

### Non-Collections

variables with 1 value

```python
number = 2
number_squared = number*number
```

number is variable. but not a list.

### Lists of lists

```python
identity_matrix = [ [1,0,0], [0,1,0], [0,0,1] ]
special_array = [ 1, [2, 3] ]
```

### Empty Lists

```python
empty_list = []
```

### For Loop

```python
numbers = [ 11, 23, 37 ]
for item in numbers:
    print(item)
# 11
# 23
# 37
```

### Indexer Of List

We can get an item from a list based on its position/index:

```python
numbers = [ 11, 23, 37 ]
first_number = numbers[0]
print(first_number)
```

### Lists Are Mutable

- strings are `immutable` (cannot change once created)
- lists are `mutable` (contents can change after created)

Example:

```python
name = "Winston"
name[0] = 'A'
```

### Range

Example:

```python
indexes = range(5)
print(indexes) # [0,1,2,3,4]
```

## Working With Lists

### Concatenating Lists

lists can be joined together like strings

```python
name = "World"
greeting = "Hello"
msg = greeting + name
print(msg)
```

```python
some_numbers = [1,2,3]
other_numbers = [2,4,6]
all_numbers = some_numbers + other_numbers

print(all_numbers)
```

### Slicing Lists

Recall:
we learned how to slice a string (lesson-05)

We can apply the same thing to lists in general:

```python
numbers = [ 2, 3, 5, 7, 11, 13 ]
last_two_numbers = numbers[-2:]
print(last_two_numbers) # [11,13]

first_two_numbers = numbers[:2]
print(first_two_numbers) # [2,3]

numbers_third_to_fifth = numbers[2:5]
print(numbers_third_to_fifth) # [5,7,11]
```

### List Methods

**The following is taken from official [documentation](https://docs.python.org/3/tutorial/datastructures.html). Attempt to read and understand what each method does. More examples can be found in the documentation.**

The list data type has some more methods. Here are all of the methods of list objects:

`list.append(x)`
Add an item to the end of the list. Equivalent to `a[len(a):] = [x]`.

`list.extend(iterable)`
Extend the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`.

`list.insert(i, x)`
Insert an item at a given position, `x`. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the **front of the list**, and `a.insert(len(a), x)` is equivalent to a.append(x).

`list.remove(x)`
Remove the first item from the list **whose value is equal to x**. It raises a ValueError if there is no such item.

`list.pop([i])`
Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

`list.clear()`
Remove all items from the list. Equivalent to `del a[:]`.

`list.index(x[, start[, end]])`
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

`list.count(x)`
Return the number of times x appears in the list.

`list.sort(\*, key=None, reverse=False)`
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

`list.reverse()`
Reverse the elements of the list in place.

`list.copy()`
Return a shallow copy of the list. Equivalent to `a[:]`.

### Build List From Scratch

The following code creates a new empty list, then adds items into that list.

```python
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff) # ['book', 99]
```

### Is Something In My List?

```python
numbers = [ 2, 3, 5]
print(3 in numbers) # True
print(3 not in numbers) # False

if 3 in numbers:
    print("3 is in my list")
```

### Lists Are In Order

Each item in a list is in an ordered position. `[1, 2, 3]`
When iterating through them, we iterate from the first position to the next, to the next.

### Built-in Functions And Lists

Some built-in functions take in lists as arguments:

```python
numbers = [11, 17, 23, 7]
length_of_numbers = len(numbers)
print(length_of_numbers) # 3
max_of_numbers = max(numbers)
print(max_of_numbers) # 23
min_of_numbers = min(numbers)
print(min_of_numbers) # 7
sum_of_numbers = sum(numbers)
print(f"11+17+23+7 = {sum_of_numbers}") # 11+17+23+7 = 58
avg_of_numbers = sum(numbers)/len(numbers)
print(f"(11+17+23+7)/4 = {avg_of_numbers}") # (11+17+23+7)/4 = 14.5

```

### Difference In Memory


