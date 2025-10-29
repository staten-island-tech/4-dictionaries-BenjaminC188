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
        print(index, ":", item)
while best_buy_items:
        purchase = input("Purchase a item:")
        cart = []
        totalprice = []
        cart.append(purchase)
        if input == 'TV':
            print(cart, totalprice + 429.99)
        elif input == 'IPhone':
            print(cart, totalprice + 1199.99)
        elif input == 'IPad':
            print(cart, totalprice + 254.99)
        elif input == 'continue':
              print('purchase another item.')
        elif input == 'done':
              print(cart and totalprice)
              break
        else:
              print("redo")
        if input == 'continue':
              print(input("Do you want to buy another item?"))
        elif input == 'done':
              print(cart and totalprice)
              

            
              





