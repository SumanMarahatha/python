class Dog:
    kind = "Canine"

    def __init__(self, name):
        self.name = name


d = Dog("buddy")
e = Dog("hello")

d.kind = "white"
d.name = "john"
e.name = "jonny"

print(d.name)
print(d.kind)

print(e.kind)
print(e.name)
