#DICTIONARY PRACTICE
'''
dic  = {"softy": ["apple", 10, "apple juice", 500], "harshita": ["mango", 8,"mango shake", 200], "pince": ["khajoor", 12, "khajur shake", 1000]}
#CALLING THE DICTIONARY BEFORE DATA MAUPULATION
# print(dic.items())
#FOR FINDING THE TOTAL KEYS IN A DICTIONARY
print(len(dic.keys()))
totals = []
for a in dic.values():
    x = 0
    x += a[1] * a[3]
    totals.append(x)
print(totals)
print(sum(totals))
# Initialize a listto store individual totals


#FOR CHANGING THE ENTIRE VALUE OF SOFTY OR ANY KEY
dic['softy'] = ['bananan']
print(dic)

def change_q(name, new_quantity):
    dic[name][1] = new_quantity
    print(dic[name])

#CALLING THE FUNCTION
change_q("pince", 4)


#Extending items to the dicitonary
dic['softy'].extend(['rasgulla', 60])
print(dic['softy'])
dic.pop('softy')
print(dic)
print('\n')

#THE NEW DICTIONARY WITH THE UPDATED QUANTITY
#print(dic.items())
# '''


# '''
class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = {}
        print(
            f"Your cart with {name.upper()} has been created successfully.\nCurrently your cart is empty add items now.\n{self.cart}")

    # CODE TO ADD ITEMS IN THE CART AND PER UNIT PRICE
    def adding(self, item, quantity=0, price=0):
        # self.item = item
        # self.quantity = quantity
        # self.price = price
        if item not in self.cart:
            n_cart = {item: [quantity, price]}
            self.cart.update(n_cart)
            print(
                item.upper() + f" with {quantity} quantity at a price of {price} per unit has been added to {self.name}'s cart.")
        else:
            print(f"ITEM {item.upper()} ALREADY IN CART!!\nYou can remove item or update quantity/price.")

    # REMOVING AN ITEM
    def removing(self, item):
        if item in self.cart:
            self.cart.pop(item)
            print(item.upper() + ' has been removed from the cart successfully...')
        else:
            print("NO such items exists ")

    # UPDATING AN ITEM
    def update(self, item, new_quantity, new_price = 0):
        old_quantity = self.cart[item][0]
        old_price = self.cart[item][1]
        self.cart[item][0] = new_quantity

        if new_price != 0:
            self.cart[item][1] = new_price
        elif new_price == 0:
            self.cart[item][1] = old_price

        if new_quantity >= old_quantity:
            print(
                f"Item {item.upper()} updated successfully.\nQuantity increased from {old_quantity} to {new_quantity}")
        else:
            print(f"Item {item.upper()} updated successfully.\nQuantity decresed from {old_quantity} to {new_quantity}")
            # CODE TO SEE THE ITEMS IN THE CART

    def show(self):
        x = len(self.cart.keys())
        total_quantity = []
        total_price = []
        for e_item in self.cart.values():
            semi_total_price = 0
            semi_total_quantity = 0
            semi_total_price += e_item[0] * e_item[1]
            semi_total_quantity += e_item[0]
            total_price.append(semi_total_price)
            total_quantity.append(semi_total_quantity)
        print(
            f"There are total {x} items in your cart\nwith total quantity of {sum(total_quantity)} units\nYour total amount is Rs.{sum(total_price)} .\n{self.cart}")




cla = shopping('naresh')

cla.adding('aaloo')
cla.adding('baigan', 4, 30)
cla.adding('rasgulla', 50, 8)
# cla.removing('baigan')
cla.removing('asdadasd')
cla.update("aaloo", 4)
cla.update("baigan", 12)
cla.update("rasgulla", 48, 9)
cla.adding('aaloo')
cla.show()
# '''