def calculate_total_amount():
    total_amount = 0.0
    
    while True:
        price = input("Enter the price of the item (or type 'finish' to end): ")
        
        if price.lower() == "finish":
            break
        
        try:
            total_amount += float(price)
        except ValueError:
            print("Please enter a valid price.")
    
    print(f"The total amount is: ${total_amount:.2f}")

# Call the function to calculate the total amount
calculate_total_amount()
