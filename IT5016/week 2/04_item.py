item1 = 10
item2 = 20
item3 = 30
# item1 = float(input("Enter the price for item1:"))
# item2 = float(input("Enter the price for item2:"))
# item3 = float(input("Enter the price for item3:"))

subtotal = item1 + item2 + item3
# subtotal = 10 + 20 + 30
salesGST = subtotal * 0.15
total = subtotal + salesGST
print("your purchase total is $",total,sep="")