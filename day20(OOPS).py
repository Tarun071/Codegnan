# class dog():
#     def __init__(self,hair,breed,color):
#         self.hair=hair
#         self.breed=breed
#         self.color=color
# d1=dog("long","pomerean","white")
# print(d1.hair)


# class name():
#     def id(self):
#         n="Tarun"
#         print(n)
# s1=name()
# s1.id()

class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def info(self):
        return f"{self.brand} {self.model} {self.year}"

c1=car("Audi","R8",2004)
print(c1)