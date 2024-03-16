class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print("Hi i am " + str(self.name) + " and my age is " + str(self.age) + " years old")


class Dog(Animal):
    def __init__(self, name, age, dog_type):
        Animal.__init__(self, name, age)
        self.dog_type = dog_type
    
    def yell(self):
        print("whaf whaffffffff")

    def dog_type_method(self):
        print("Hi my name is " + self.name + " and type is " + self.dog_type)


class Cat(Animal):
    def __init__(self, name, age, skin_color):
        Animal.__init__(self, name, age)
        self.skin_color = skin_color
    
    def yell(self):
        print("mew")

    def color(self):
        print("Hi my name is " + self.name + " and my skin color is " + self.skin_color)










animal1 = Dog("bolt" , 5, "bulldog")
animal1.talk()
animal1.yell()
animal1.dog_type_method()

animal2 = Cat("lucci" , 7 , "white")
animal2.talk()
animal2.yell()
animal2.color()