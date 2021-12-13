class Mammal:
    def walk(self):
        print("walk")





class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_happy(self):
        print("Be happy")

cat1 = Cat()
cat1.be_happy      

dog1 = Dog()
dog1.walk()
    

