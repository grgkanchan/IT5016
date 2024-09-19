def display_intro():
    message = "hey i am kanchan"
    print(message)
    
# display_intro()


def display_BMI (weight,height):
   BMI = weight/ (height/100)**2
   return BMI

weight =int(input("Enter weight:"))
height = int(input("Enter height:"))
print (display_BMI(weight,height))



   
    
    