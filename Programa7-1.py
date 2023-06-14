#Programacion orientada a objetos
class person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def age(self):
        return f"{self._age} anios"
    
    @age.setter
    def age(self, age):
        self._age = age
        
    def saludo(self):
        print(f"hola mi nombre es {self.name} y mi edad es {self.age}")
        
p1 = person("daniel", 29)
print(f"Edad es {p1.age}")
p1.saludo()