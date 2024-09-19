# def main():
#     a = 42 
#     b = 17
#     c = 94
#     if a > b and a > c:
#         print("you")
#     if not (a > b and a > c):
#         print("cannot")  
#     if a  > b or a > c:
#         print("Tuna")
#     if not(a > b or a > c):
#         print("fish")   
        
#     main()    
    
    
    
def get_price(child,adult):
        child_price = 10
        adult_price = 25
        group_size = 14
        group_rate = 0.9
        
        cost = (child * child_price + adult_price)
        if child + adult >group_size:
            cost = cost * group_rate
        return cost
def main():
         num_child = int(input("Enter the number of the children:"))   
         num_adult = int(input("Enter the number of the adult:"))
         cost = get_price(num_child,num_adult)
         print("the cost of your tickets is : $" + str(cost))
main()    
            
              