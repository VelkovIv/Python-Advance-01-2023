def shopping_cart(*products):
    products_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    result = ''

    for product in products:
        if product == "Stop":
            break
        meal, product = product[0], product[1]

        if meal == 'Soup' and len(products_dict['Soup']) < 3:
            if product not in products_dict['Soup']:
                products_dict[meal].append(product)

        elif meal == 'Pizza' and len(products_dict['Pizza']) < 4:
            if product not in products_dict['Pizza']:
                products_dict[meal].append(product)

        elif meal == 'Dessert' and len(products_dict['Dessert']) < 2:
            if product not in products_dict['Dessert']:
                products_dict[meal].append(product)

    if len(products_dict['Soup']) == 0 and len(products_dict['Pizza']) == 0 and len(products_dict['Dessert']) == 0:
        result = 'No products in the cart!'

    else:
        for meal, products in sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f'{meal}:\n'
            for product in sorted(products):
                result += f' - {product}\n'

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
