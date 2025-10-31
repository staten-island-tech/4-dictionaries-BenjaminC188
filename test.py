best_buy_items = [
{
    'name': "TV",
    'price': 429.99,
    'department': "Electronics",
    'description': "A big screen."
},

{
    'name': "IPhone",
    'price': 1199.99,
    'department': "Electronics",
    'description': "A small screen."
},

{
    'name': "IPad",
    'price': 254.99,
    'department': "Electronics",
    'description': "A medium screen."
}
]

"""for index, item in enumerate(best_buy_items):
    print(item['name'])"""

print(best_buy_items)
cart = []
totalprice = 0
print("Purchase an item: TV, IPhone, or IPad.")
while best_buy_items:
    purchase = input("Continue shopping or done?")
    if purchase == "TV":
        item = best_buy_items[0]
        cart.append(item['name'])
        totalprice += item["price"]
        print("you added:", item)
    elif purchase == "IPhone":
        item = best_buy_items[1]
        cart.append(item['name'])
        totalprice += item["price"]
        print("you added:", item)
    elif purchase == "IPad":
        item = best_buy_items[2]
        cart.append(item['name'])
        totalprice += item["price"]
        print("you added:", item)
    elif purchase == "continue":
        print("purchase another item.")
        continue
    elif purchase == "done":
        print("items in cart:")
        for item in cart:
            print(item)
        print("total price of items:", totalprice)
        break
    else:
        print("item not found.")
