my_list = ['яблоко', 'ананас', 'арбуз', 'манго', 'груша', 'мандарин']
print(my_list)
print(my_list[::len(my_list)-1])  # Первый и последний элементы списка my_list.
print(my_list[3:5])  # Если по индексу, где 5-й не включён (т.к. до пятого элементов)
my_list[3] = 'персик'  # 3-й по индексу
print(my_list)

my_dict = {'house': 'дом', 'apple': 'яблоко', 'fire': 'огонь', 'side': 'сторона'}
print(my_dict)
print(my_dict.get('fire'))
my_dict['water'] = 'вода'
print(my_dict)
