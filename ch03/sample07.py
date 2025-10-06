import copy

list_value = ['1', '2', '3','4', '5', '6', '7', '8']
new_list_value = list_value[:]

print(list_value)
print(new_list_value)

list_value[0] = '11'

print('-'*20)
print(list_value)
print(new_list_value)

print('='*20)
list_value = [['1', '2'], ['3','4'], ['5', '6'], ['7', '8']]
#new_list_value = list_value[:]
new_list_value = copy.deepcopy(list_value)

print(list_value)
print(new_list_value)

list_value[0][0] = '11'

print('-'*20)
print(list_value)
print(new_list_value)

del new_list_value
#print(new_list_value)