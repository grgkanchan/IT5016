
class Car:
    def __init__(self,color,model,year):
        self.color = color
        self.model = model
        self.year = year
        
    def drive(self):
        print(f"The {self.color},{self.model},{self.model}.")
    
car1 = Car("black","Tesla Model 5","2023")
car1.drive()


       
        
        
        
        