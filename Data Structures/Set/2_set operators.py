# Set operators
'''Both set and frozen set has the following operators.
Create two sets s1 and s2 using following procudure'''
s1 = set()
s2 = set()
for i in range(2, 9):
    s1.add(i)
for i in range(4, 9):
    s2.add(i)
print("s1= ",s1, '\n','s2= ',s2, sep="")

# s1 == s2
# set s1 is same as set s2
print('s1 == s2:', s1==s2)

# s1 != s2
# set s1 is not same as set s2
print('s1 != s2:', s1 != s2)

# s1 <= s2
# set s1 is subset of set s2
print('s1 <= s2:', s1 <= s2)

# s1 > s2
# set s1 is proper superset of s2
print('s1 > s2:', s1 > s2)

# s1 | s2
# gives new set which contains the union of s1 and s2
print('s1 | s2:', s1 | s2)

# s1 & s2
# gives new set which contains the intersection of s1 and s2
print('s1 & s2:', s1 & s2)

# s1 - s2
# gives new set which contains the elements in s1 but not in s2
print('s1 - s2:', s1 - s2)

# s1 ^ s2
# gives the set of elements either in s1 or s2
print('s1 ^ s2:', s1 ^ s2)