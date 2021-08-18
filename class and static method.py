# class method
class Person:
    number_of_people =0
    def __init__ (self, name):
      self.name = name
      Person.number_of_people= Person.number_of_people + 1
    def add(self):
        print('add method')
    @classmethod
    def get_num_of_ppl(cls):
       return cls.number_of_people


p1= Person('suraj')
p2= Person('honey')
print(p1.name)
print(Person.get_num_of_ppl())

# static
class Math:
 pi =3.14

 def add(self,x):
     return x+1
 @classmethod
 def add_10(cls):
     return cls.pi
 @staticmethod
 def add_5(x):
     return x+5
x=20
print(id(x))