

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"Fruit('{self.name}', '{self.color}')"

print(Fruit("mango", "orange"))
# <__main__.Fruit object at 0x102bdac10>
# this is not developer friendly during debugging
# so we add a repr dunder methd

# try again
# Fruit('mango', 'orange')
# this is just best practice


### Add difference between repr str dunder methods