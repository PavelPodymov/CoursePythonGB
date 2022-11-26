"""
For checking
*Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение
— список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
goods_ex = [
    (1, {'name': 'computer', 'price': 20000, 'quantity': 5, 'unit': 'pieces'}),
    (2, {'name': 'printer', 'price': 6000, 'quantity': 2, 'unit': 'pieces'}),
    (3, {'name': 'scanner', 'price': 2000, 'quantity': 7, 'unit': 'pieces'})
]

START = True
goods = []
COUNT = 0
while START:
    y_n = input("If you don't want to continue write - n: ").lower()
    if y_n == 'n':
        START = False
    else:
        name_s = input("name of goods: ")
        price_s = int(input("price: "))
        quantity_s = int(input("quantity: "))
        COUNT += 1
        goods.append((COUNT, {'name': name_s,
                              'price': price_s,
                              'quantity': quantity_s,
                              'unit': 'pieces'}))

new_dict = {}
for i in goods[0][1]:
    new_dict[i] = []

for key in new_dict:
    dict_list = []
    for i in goods:
        value = i[1].get(key)
        dict_list.append(value)
        if key != 'unit':
            new_dict[key] = dict_list
        else:
            new_dict[key] = ['pieces']

print(new_dict)
