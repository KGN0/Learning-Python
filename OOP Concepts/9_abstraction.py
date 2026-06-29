'''Abstraction is the synonym for data hiding. Here data hiding can be implemented in methods by writing no code in the methods.
    That means empty methods are  written in one class. These methods are implemented in another class with the help of inheritence.'''
# Example
class Built:
    def taste(self):
        raise NotImplementedError()
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class Mango(Built):
    def taste(self):
        return "Sweet"
    def rich(self):
        return "Vitamin A"
    def color(self):
        return "Yellow"
obj = Mango()
print(obj.taste(),"\n", obj.rich(), "\n", obj.color(), sep="")