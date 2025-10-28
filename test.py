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

        

for index, item in enumerate(best_buy_items):
        print(index, ":", item["name"])
for index, item in enumerate(best_buy_items):
            print(index, ":", item["price"])
def cart():
    cart = []
    while best_buy_items:
        purchase = input("Purchase a item:")
        cart.append(purchase)
        if input == 'TV':
            print(cart, "Continue shopping or are you done?")
        elif input == 'IPhone':
            print(cart)
        elif input == 'IPad':
            print(cart)
        elif input == continue:
              
        elif input == 'done':
              print(cart)




