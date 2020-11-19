# Определяем 3 словаря

d1 = {
    'a': 'A',
    'b': 'B',
    'c': 'C'
}

d2 = {
    'b': 'B',
    'a': 'A',
    'c': 'C'
}

d3 = {
    'a': 'A',
    'b': 'B',
    'c': 'C'
}

print(d1 == d2) # Обычные словари будут Екгу потому что сравнивается смылс, а не сортировка
print(d1 == d3)

for k, v in d2.items():
    print(k,v)

from collections import OrderedDict

# Создаем отсортированные словари
dic1 = OrderedDict() 
dic1['a']= 'A'
dic1['b']= 'B'
dic1['c']= 'C'


dic2 = OrderedDict() 
dic2['b']= 'B'
dic2['a']= 'A'
dic2['c']= 'C'


dic3 = OrderedDict()
dic3['a']= 'A'
dic3['b']= 'B'
dic3['c']= 'C' 

# Сравниваем словари. Отсортированные словари будут сравниваться по поряду
print (dic1 == dic2)
print (dic1 == dic3)