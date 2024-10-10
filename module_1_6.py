my_dict = {'Ivan' : 2000 , 'Julia' : 1994}
print(my_dict)
print(my_dict['Julia'])
print(my_dict.get('Sanya'))
a = my_dict.pop('Ivan')
print(a)
my_dict['Alex'] = 1998
print(my_dict)
my_dict.update({'Anton' : 2001 , 'Stas' : 2002})
print(my_dict)

my_set = {1, 1 , 2, 3, 3, 2, 4, 4, 'book', 'table',  'book'}
print(my_set)
my_set.add(8)
my_set.remove('book')
print(my_set)