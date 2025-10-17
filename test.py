best_buy_items = ()
{
    'name': "TV",
    'price': 429.99,
    'department': "Electronics",
    'description': "A big screen."
}

{
    'name': "IPhone",
    'price': 1199.99,
    'department': "Electronics",
    'description': "A small screen."
}

{
    'name': "IPad",
    'price': 254.99,
    'department': "Electronics",
    'description': "A medium screen."
}
def cart():
    cart = []
    print(best_buy_items ['name'] ['price'] ['department'] ['description'])
    print("purchase a item")
    while input == ['TV']:
        print(best_buy_items[0])
        print("Do you want to add this item to cart?")
    if input == 'yes':
        cart.append(best_buy_items[0])
    elif input == ['IPhone']:
        print(best_buy_items[1])
        print("Do you want to add this item to cart?")
    if input == 'yes':
        cart.append(best_buy_items[1])
    elif input == ['IPad']:
        print(best_buy_items[2])
        print("Do you want to add this item to cart?")
    if input == 'yes':
        cart.append(best_buy_items[2])