# Iterating through a dictionary
# using a for loop we can iterate though each key in a dictionary
# Example
d1 = {'A':'Arrow', 'B':'Banana', 'C':'Camel', 'D':'Donkey', 'E':'Elephant'}
for key in d1:
    print(key,'-', d1[key])
print()
days = {0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thur', 5:'Fri', 6:'Sat'}
for key in days:
    print(key, ":", days[key])

# Sorting a dictionary
'''The items in dictionary can be sorted using sorted() funtion.
-   fromkeys() function is used to create a dictionary from sequence of values.
    The value 0 is assigned for all keys.
-   Each item is accessed iteratively using for loop that iterate though each key in a dictionary'''

# Example
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.keys())))

