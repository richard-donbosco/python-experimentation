class Animals():
    def __init__(self, name, age, animal_type):
        self.name= name
        self.age= age
        self.animal_type= animal_type
    

class Dog(Animals):
    def __init__(self, name, age, breed, avg_height):
        self.breed = breed 
        self.avg_height= avg_height
        super().__init__(name, age, "dog")
    
    def __repr__(self):
        return "Class Dog: Attributes --> name,age,breed,avg_height ; Methods--> None"
    
    def __str__(self):
        return "The dog's name is {}\nThe dog's age is {}\nThe dog's breed is {} ".format(self.name, self.age, self.breed)


Class HerdingGroups(Dogs):
    """
    Up until 1983, the breeds in the Herding Group were part of the Working Group. 
    All Herding breeds share an instinctual ability to control the movement of other animals. 
    These breeds were developed to gather, herd and protect livestock. 
    Today, some like the Belgian Malinois and the German Shepherd Dog are commonly used for police and protection work. 
    The herding instinct in these breeds is so strong that Herding breeds have been known to gently herd their owners, especially the children of the family. 
    In general, these intelligent dogs make excellent companions and respond beautifully to training exercises.
    """

    def __init__(self, name, age, breed, avg_height, height, weight, life_expectancy):
        self.height= height
        self.weight= weight
        self.life_expectancy= life_expectancy
        super().__init__(name, age, breed, avg_height)




    
