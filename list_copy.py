import copy

spam = ['A',
'B',
'C',
'D']
cheese = copy.deepcopy(spam)
cheese.append('E')

print(spam)
print(cheese)