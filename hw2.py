from pprint import pprint
from logger_path import decorator
cook_book = {}
lister_1 = []

with open("recipes.txt", encoding="utf8") as file:
    for line in file:
        dish = line.strip()
        cook_book[dish] = []
        amounti_ngredients = int(file.readline())
        for i in range(amounti_ngredients):
            ingredients = file.readline().strip().split("|")
            cook_book[dish].append({'ingredient_name': ingredients[0],'quantity': ingredients[1], 'measure': ingredients[2]})
        file.readline()
    pprint(cook_book)
path = 'logger.txt'
@decorator(path)
def get_shop_list_by_dishes(dishes, count_persons):

    ingredient = {}

    for dish in cook_book:
        if dish in dishes:
            for ingredients in cook_book[dish]:
                count_ingredients = {}
                count_ingredients['quantity'] = int(ingredients['quantity']) * count_persons
                count_ingredients['measure'] = ingredients['measure']
                count_ingredients['quantity'] = count_ingredients['quantity']
                name = ingredients['ingredient_name']
                if ingredients['ingredient_name'] in ingredient.keys():
                    count = ingredient[name]
                    count_ingredients['quantity'] = int(count['quantity']) + int(count_ingredients['quantity'])
                    ingredient[ingredients['ingredient_name']] = count_ingredients
                else:
                    ingredient[name] = count_ingredients
    pprint(ingredient)

get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Картофельное пюре'], 4)

