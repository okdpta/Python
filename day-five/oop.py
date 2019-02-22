class Dog:
    
    species = "mammal"

    def __init__(self,the_sound):
        self.sound_made = the_sound
    
    def sound(self):
        print(self.sound_made)

    def bite (self):
        self.sound()
        print("Bite")
    
    def identify_yourself(self):
        print("I am a" + self.species)

class Bulldog(Dog):
    def run(self):
        speed = "10km/hr"      
        print("i run at 10km/hr")



my_dog = Dog("woof")
my_second_dog = Dog("woooooooooooffffffff")

my_bulldog = Bulldog("wooorrrf")

my_bulldog.sound()


