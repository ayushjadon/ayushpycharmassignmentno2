class Cat:
    pass
    def speak_once (self):
     print("meau")
    def set_breed(self,breed):
        self.breed =breed
    def get_breed(self):
        return self.breed
    def walk_twice(self):
     print("walk")
d =Cat()
d.set_breed("indian cat")
print(type(d.speak_once))
print(type(d.walk_twice))
d.speak_once()
d.walk_twice()
print(d.get_breed())
print(type(d))
