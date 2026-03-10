#1
tables = {1: ['Jho', False], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
def assign_table(table_number, name, vip_status = False):
    tables[table_number] = [name, vip_status]
assign_table(6,'Yoni')
assign_table(4,'Карла')
print(tables)

#2
def print_order(*order_items):
    print(order_items)
print_order('Orange Juice','Apple Juice','Scrambled Eggs','Pancakes')

#3
tables1 = {1:{'name': 'Jiho', 'vip_status': False, 'order': 'Orange Juice, Apple Juice'}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
def assign_and_print_order(table_number, *order_items):
    tables1[table_number]['order'] = order_items
    for x in order_items:
        print(x)
assign_table(2, 'Arwa', vip_status = True)
assign_and_print_order(2, 'Стейк', 'Морской окунь', 'Бутылка вина')

#4
tables2 = { 1:{'name': 'Chioma', 'vip_status': False, 'order': {'drinks': 'Orange Juice, Apple Juice', 'food_items': 'Pancakes'}}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}}
def assign_food_items(**order_items):
    food = order_items.get('food')
    drink = order_items.get('drinks')
    print(food, drink)
assign_food_items(food = 'Pancakes, Poached Egg', drinks = 'Water')

#5
table_7_total = [534.50, 20.0, 5]
def calculate_price_per_person(total,tip,split):
    total_tip = total*(tip/100)
    split_price = (total + total_tip) / split
    print(split_price)
calculate_price_per_person(*table_7_total)
