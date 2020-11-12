class Point:
    def __init__(self, x, y):   #construct or create an object.
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

        
point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
