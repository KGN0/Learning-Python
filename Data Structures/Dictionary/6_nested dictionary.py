# Nested Dictionaries
'''A nested nested dictionary inside a dictionary. It's a collection of dictionaries into one single dictionary
Syntax: nested_dict = 
{
    'dictA':{'key1':'value1'}
    'dictB':{'key2':'value2'}
}
'''
# Creating nested dictionary
dict1 = {'child1':{'name':'Emil','year':2004},
         'child2':{'name':'Tobias', 'year':2007},
         'child3':{'name':'Linus', 'year':2011}
         }
print('nested dict1:', dict1)

# Acessing nested dictionary
print("dict1['child1']=",dict1['child1'])
print('dict1["child2"]["year"]=', dict1['child2']['year'])

# Add element to a Nested dictionary
database = {1:{'name':'Ruby', 'age':47, 'sex':'Female'},
            2:{'name':'Mary', 'age':22, 'sex':'Female'}
            }
print('database=', database)

database[3] = {}
database[3]['name'] = 'Mahi'
database[3]['age'] = 24
database[3]['sex'] = 'Male'
print('database=', database)

database[4] = {'name':'Hari', 'age':20, 'sex':'Male', 'married':'No'}
# print(database)
for key in database:
    print(key, ":", database[key])

# delete elements from a nested dictionary
# Example
del database[4]['married']
del database[3]
print(database)

# iterating through nested dictionaries
for key, info in database.items():
    print('Person ID:', key)
    for kee in info:
        print(" ",kee, ":", info[kee])