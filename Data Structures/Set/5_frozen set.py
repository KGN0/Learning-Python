# Frozen set
''' The frozen sets are the immutable form of the normal sets, i.e., the items of the frozen set cannot be changed.
    The forzenset() method is used to create the frozenset object. The iterable sequence is passed into 
    this method which is converted into the frozen set as a return type of the method '''
frozen_set = frozenset(['h', 'a', 'i'])
print('Frozen set')
# frozen_set.add('i')  # raise error

# frozenset methods
# the supported methods are
frozenset1 = frozenset([10, 20, 30, 40, 50])
frozenset2 = frozenset([30, 30, 10, 60, 80])
print(frozenset1.union(frozenset2))
print(frozenset1.difference(frozenset2))
print(frozenset1.symmetric_difference(frozenset2))
print(frozenset1.intersection(frozenset2))

print(frozenset1.isdisjoint(frozenset2))
print(frozenset1.issubset(frozenset2))
print(frozenset1.issuperset(frozenset2))

frozenset3 = frozenset1.copy()
print(frozenset3)