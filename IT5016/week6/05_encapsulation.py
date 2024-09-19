class Person:
    def __init__(self):
        self.A ="James"
        self.__B ="james Bond"
        
    def PrintName(self):
        print(self.A) 
        print(self.__B)
    
P = Person()
P.A 
P.__B 


   