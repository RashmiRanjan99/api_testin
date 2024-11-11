# class Dog:
#     def sound(self):
#         return "Bark"

# class Cat:
#     def sound(self):
#         return "Meow"

# def make_sound(animal):
#     print(animal.sound())

# d = Dog()
# c = Cat()
# make_sound(d)
# make_sound(c)
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")

obj = B()
obj.show()