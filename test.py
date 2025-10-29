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


cart = []
totalprice = 0
while True:
    purchase = input("Purchase an item (TV, IPhone, IPad): ")

    if purchase == "TV":
        item = best_buy_items[0]
        cart.append(item)
        totalprice += item["price"]
        print("You added:", item)
    elif purchase == "IPhone":
        item = best_buy_items[1]
        cart.append(item)
        totalprice += item["price"]
        print("You added:", item)
    elif purchase == "IPad":
        item = best_buy_items[2]
        cart.append(item)
        totalprice += item["price"]
        print("You added:", item)
    elif purchase == "continue":
        print("Purchase another item.")
        continue
    elif purchase == "done":
        print("Items in cart:")
        for item in cart:
            print(item)
        print("Total price:", totalprice)
        break
    else:
        print("Invalid input. Try again.")
              

            
              





