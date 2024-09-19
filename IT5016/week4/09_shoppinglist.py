"""
SHOPPING_list():
"""

def shopping_list():
    shopping_list = [] # it is a list that stores values.
    total_price = 0
    while True:
       item = input("Enter the name of the item (or type 'done' to finish):")
       if item.lower() == 'done':
        break
    try:
        price = float(input(f"Enter the price of '{item}': "))
        shopping_list.append((item,price))
        total_price += price
    except ValueError:
        price("Invalid input.please enter a numeric value for the price.")
    
    return shopping_list,total_price

def main():
    print("Welcome to the shopping list program")
    shoopping_list , total_price = shopping_list()
    
    if not shoopping_list:
        price("No items were entered")
    else:
        print("\nshopping list:")  
        for item, price in  shoopping_list:
            print(f"{item},${price:.2f}")
            print(f"\nTotal price: ${total_price:.2f}")    
            
main()        
            
          
           