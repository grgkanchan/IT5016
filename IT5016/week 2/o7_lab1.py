"""
calculate the cost of the books 
calculate the shipping cost 
calculate the total wholesale cost 
Author = kanchan 
"""

cover_price = 24.95
Shipping_cost =3
Discount = 0.40
additional_copy = 60
Shipping_cost_for_additional_copy = 0.75

import math 
Discount_price = cover_price * Discount # #Discount per book
 
 #discount cost
cost_after_doscount = cover_price - Discount_price #per book
total_cost_after_discount = cost_after_doscount * additional_copy

total_shipping_cost = Shipping_cost + Shipping_cost_for_additional_copy * (additional_copy-1)
total_wholesale_cost = total_cost_after_discount + total_shipping_cost

print("the total wholesale cost for 60 copies is $", total_wholesale_cost,sep="")





