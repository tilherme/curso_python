import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [ 1,2,3]
}

d2 = copy.deepcopy(d1)

d2['c1']= 'gui'

print(d2['l1']) 

# print(d1)
# print(d2)


