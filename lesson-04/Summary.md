# Summary

To recap the things we learned today:

## 1. Github Install

Python 3.9 (check "add python to environment variables")
Visual studio code
    Opening terminal
    Selecting color theme
    Installing extensions
    Selecting linter (an extension that analyses ur python file for python syntax and keywords and decides how to color code them)
    Running python

## 2. Git Repository Fork Pull Push

(Cpu, memory, storage)

## 3. Python Iterations: More Patterns

```python
#Example 1
foundAThree = False
print('Before', foundAThree)
for number in [9, 41, 12, 3, 74, 15, 100, 1000, 123, 21]:
    if (number == 3):
        foundAThree = True
        print(foundAThree, number)
        break
    #insert 'break' to go out of the loop and move out of the loop (i.e. jump to line 11)
    #insert 'continue' to skip the rest of the iteration and go back to the first line of the loop (i.e. skip line 10 and jump to line 3)
    print(foundAThree, number)
print('After', foundAThree)

#Example 2
smallest_number_so_far = None
for number in [45, 60, 10, 7, 84, 0, 87, 56, 15, 3]:
    if smallest_number_so_far is None:
        smallest_number_so_far=number
    elif number<smallest_number_so_far:
        smallest_number_so_far=number
    print(smallest_number_so_far,number)

```

## 4. Jargons

    repository / git repository := folder that is enabled with git (version control tool)
    diff (git diff)
    forking

    git commands:
    - commit
    - pull

    gitignore:
    - a list of filenames / folder names which git will ignore changes from

    branch (a version of the repository with its own history. branches can be split into subbranches and merged into 1 final branch. We use branches to manage different histories and either converge them or split them.)

    loop: something that includes many iterations
    iteration: each cycle in the loop

