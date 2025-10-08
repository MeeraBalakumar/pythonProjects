# -*- coding: utf-8 -*-#See a list of available items.

#Add items to their cart.

#See the total price.
store_items={
    "apples":1.0,
    "banana":2.1,
    "milk":5.0,
    "biscut":4.2
    }
cart = []

def display_items():
    print("\n available items:")
    for item, price in store_items.items():
        print(f"{item.title()}:${price:.2f}")
def add_to_cart():
    item=input("enter item to add to cart:").lower()
    if item in store_items:
        cart.append(item)
        print(f"{item.title()} added to cart")
    else:
        print("items not found")
def view_cart():
    if not cart:
        print("your cart is empty")
        return
    print("\n your cart:")
    total=0
    for item in cart:
        print(f"{item.title()}:${store_items[item]:.2f}")
        total+=store_items[item]
    print(f"Total:${total:.2f}")
def main():
   while True:
        print("\n1.available items\n2.add_to_cart\n3.view_cart\n4.exit")
        choice=input("choose an option:")
        if choice=="1":
           display_items()
        elif choice=="2":
            add_to_cart()
        elif choice=="3":
            view_cart()
        elif choice=="4":
            print("thanks for shopping")
            break
        else:
            print("invalid choice")
main()         
        
            
        
            
    
        
        
    
    
