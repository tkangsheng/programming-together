# Python code to demonstrate
# finding whether element
# exists in listof list
  
# initialising nested lists
ini_list = [[1, 2, 5, 10, 7],
            [4, 3, 4, 3, 21],
            [45, 65, 8, 8, 9, 9]]
  
elem_to_find = 8
elem_to_find1 = 0
  
# element exists in listof listor not?
res1 = any(elem_to_find in sublist for sublist in ini_list)
res2 = any(elem_to_find1 in sublist for sublist in ini_list)
  
# printing result
print(str(res1), "\n", str(res2))
