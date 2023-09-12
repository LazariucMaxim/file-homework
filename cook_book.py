with open('recipes.txt') as recipes:
    cook_book = {}
    counter = 0
    for line in recipes:
        line = line.strip()
        if not line:
            continue
        elif counter == 0:
            dish = line
            cook_book[dish] = []
        elif counter < 0:
            counter = int(line)+1
        else:
            ingredient = list(map(lambda x: x.isdigit() and int(x) or x, line.split(' | ')))
            ingredient_archetype = ['ingredient_name', 'quantity', 'measure']
            cook_book[dish].append(dict(zip(ingredient_archetype, ingredient)))
        counter -= 1


def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        for ing_name, ing_quantity, ing_measure in map(lambda x: list(x.values()), cook_book[dish]):
            if ing_name in all_ingredients:
                all_ingredients[ing_name]['quantity'] += ing_quantity * person_count
            else:
                all_ingredients[ing_name] = {'quantity': ing_quantity * person_count,
                                             'measure': ing_measure}
    return all_ingredients
