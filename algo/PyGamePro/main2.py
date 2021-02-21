class Robot:
    def __init__(self, speed) -> None:
        self. speed = speed
        self.x = 0
        self.y = 0
    
    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

class Terminator(Robot):
    def __init__(self, speed, name) -> None:
        super().__init__(speed)
        self.name = name

    def move_left(self):
        self.x -= self.speed * 2

    def move_right(self):
        self.x += self.speed * 2

terminator = Terminator(10, "R2")
print("x =", terminator.x, "y =", terminator.y)
terminator.move_left()
print("x =", terminator.x, "y =", terminator.y)
print(terminator.name)