class vehicle:
    def __init__(self) -> None:
        pass
    
    def  start(self):
        print("vehicle started")
        
    def  stop(self):
        print("Vehicle stopped")  
        
class Car(vehicle):
    def hork(self):
        print(" Honk! Honk!")  
        
my_car = Car()
my_car.start()
my_car.hork()
my_car.stop()       
        
         
        