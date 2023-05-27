#3. Vehicle Class Hierarchy
class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def start(self):
        print("Vehicle has started")
    def stop(self):
        print("Vehicle is stationary")
    def info(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
        
class Car(vehicle):
    def __init__(self,make,model,year,num_doors,fuel_type):
        super().__init__(make,model,year)
        self.num_doors=num_doors
        self.fuel_type=fuel_type
class Motorcycle(vehicle):
    def __init__(self,make,model,year,top_speed):
        super().__init__(make,model,year)
        self.top_speed=top_speed
class Truck(vehicle):
    def __init__(self,make,model,year,cargo_capacity,num_axles):
        super().__init__(make,model,year)
        self.cargo_capacity=cargo_capacity
        self.num_axles=num_axles
        
myCar=Car("Audi","A3",2023,4,"Diesel")
myCar.start()
myCar.info()
myCar.stop()
print()
myMotorcycle=Motorcycle("Vespa","vespa300",2009,120)
myMotorcycle.start()
myMotorcycle.info()
myMotorcycle.stop()
print()
myTruck=Truck("Tata","Ace",2005,"710 kgs",4)
myTruck.start()
myTruck.info()
myTruck.stop()