# Nested tuples
'''Python allows you to define a tuple inside another tuple.
This is called nested tuple'''

# Example
toppers = (('Arav', 'B.Tech', 92.8), ('Swetha', 'B.Tech', '94.6'))
for record in toppers:
    print(record)

print()

for record in toppers:
    for details in record:
        print(details, end = ", ")
    print()

for i in range(len(toppers)):
    print(toppers[i])