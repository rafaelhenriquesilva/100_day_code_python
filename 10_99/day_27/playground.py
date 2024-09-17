# Unlimted Arguments
def add(*args):
    total = 0
    for n in args:
        total += n
        
    return total

print(f'Sum multiple: {add(1,2,3,4,5,6,7,8,9,10)}')

# **kwargs arguments
# Recipe a dictionary
def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    
    
calculate(2, add=3, multiply=5)

class People:
    def __init__(self, **kw) -> None:
        self.name = kw.get('name')
        self.age = kw.get('age')
        self.email = kw.get('email')
        
        
p1 = People(name='Rafael', age=27)
print(p1.name)
print(p1.age)
print(p1.email)