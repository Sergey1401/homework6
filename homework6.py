# Практическое задание по теме: "Словари и множества"
# Работа со словарем:
my_dict = {'Sergey':1984,'Ivan':1992,'Irina':1987,'Vera':1993}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Sergey'])
print('Not existing value: ',my_dict.get('Kristina'))
my_dict.update({'Viktor':1977,'Eva':1979})
a = my_dict.pop('Ivan')
print('Deleted value: ',a)
print('Modified dictionary: ',my_dict)
print()
# Работа со множеством:
my_set ={11,'Wing',11,14.25,'Forest','Forest'}
print(my_set)
my_set.add(17)
my_set.add('Table')
my_set.discard(14.25)
print(my_set)