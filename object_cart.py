class ShoppingCart:
    def __init__(self, owner):
        self.owner = owner
        self.basket = []
        
    def add_item_to_basket(self, item_name, price, quantity):
        self.basket.append(Item(item_name, price, quantity))

    def add_to_basket(self):
        item_name = input("Enter item name to add: ")
        price = input("Enter price: ")
        quantity = input("Enter item quantity: ")
        
        self.basket.append(Item(item_name, price, quantity))

    def remove_from_basket(self):
        item_name = input("What would you like to remove: ")

        for item in self.basket:
            if item.item_name == item_name:
                self.basket.remove(item)
                break
        else:
            print("Item not found.")

    def list_basket(self):
        if len(self.basket) == 0:
            print("Basket is currently empty. Consider adding some items to it!")
        else:
            total = 0
            for item in self.basket:
                print("------")
                print(f"  {item.item_name}")
                print(f"    ${item.price:,.2f}")
                print(f"    {item.quantity}")
                total += item.price * item.quantity
            print("------")
            print(f"Total: ${total}")
        

class Item:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = float(price)
        self.quantity = float(quantity)
        
    def total(self):
        return self.price * self.quantity


def main():
    shopping_carts = []

    #create fake user
    shopping_carts.append(ShoppingCart("Slagathor"))
    shopping_carts[0].add_item_to_basket('apples', .24, 3)
    shopping_carts[0].add_item_to_basket('bananas', .24, 3)
        
    while True:

        print("Thanks for shopping at BobMart.")
        user = input("Please enter your name: ").title()
        # find user
        index = -1
        for i, cart in enumerate(shopping_carts):
            if cart.owner == user:
                index = i

        if index !=  -1: # user found
            print(f"Welcome back, {user}")
            user = shopping_carts[index]
        else: # user not found
            print("Welcome New User")
            index = len(shopping_carts)
            shopping_carts.append(ShoppingCart(user))
            user = shopping_carts[index]

        while True:
            
            user_input = input("What would you like to do? (add/remove/list/quit) ").lower()
            if user_input in {'add', 'remove', 'list', 'quit'}:
                if user_input == 'add':
                    user.add_to_basket()
                    pass
                elif user_input == 'remove':
                    user.remove_from_basket()
                    pass
                elif user_input == 'list':
                    user.list_basket()
                    pass
                elif user_input == 'quit':
                    break
            else:
                print("Unknown command.")

        user_continue = input("Would you like to continue with another user? (Y/N) ").lower()

        if user_continue == 'y':
            pass
        else:
            break
            

main()
