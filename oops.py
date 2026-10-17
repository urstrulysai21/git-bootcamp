class vehicle:
    def __init__(self):
        pass

class car: #class is a blueprint for creating the objects 
    vehicle_categorie = "Cars" #class variables are same for the all of the objects

    def __init__(self,Model,year,color):
        self.Model = Model     #instance variables are different for the each object that is being created for the object
        self.year = year
        self.color = color

    def Start(self):
        print(f"you have started the {self.Model} engine")

car1 = car("BMW",2026,"Dark Black")
car2 = car("Range Rover Sport",2026,"Dark Black")
car3 = car("Mercedes AMG Gwagon",2026,"Dark Black")
car2.Start()


print(car2.Model)
print(car.vehicle_categorie)
print(car3.vehicle_categorie)