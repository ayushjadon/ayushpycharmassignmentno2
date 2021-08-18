 #special function
class Animal:
 def __init__ (self,name,age):
    self.name = name
    self.age = age
 def kind (self):
    print('kind')

d=Animal("tom",25)

print(d.name)
print(d.age)