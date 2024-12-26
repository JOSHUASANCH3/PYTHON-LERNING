### Clases primer ejmeplo
class MyEmptyPerson:
    ##definicion de pass
    pass


print("Hola")
print(MyEmptyPerson)
print(MyEmptyPerson())


##Creacion de clase de mi persona
class MyPerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        pass


my_person = MyPerson("Joshua", "Sanchez")
print(f"{my_person.name} {my_person.surname}")


##Creacion alternatiava de la clase person
class MyPersonAlter1:
    def __init__(self, name, surname):
        self.fullname = f"{name} {surname}"

    def walk(self):
        print(f"{self.fullname} ")

    pass


my_person = MyPersonAlter1("Joshua", "Sanchez")
print(MyPersonAlter1.fullname)
MyPersonAlter1.walk()


##Creacion alternativa de la clase persona con propiedades privadas y getter
class MyPersonAlter2:
    def __init__(self, name, surname, alias="Sin alias"):
        self.fullname = f"{name} {surname} {alias}"
        self.__name = name  ##Propidad Privada

    def walk(self):
        print(f"{self.fullname}")

    def get_name(self):
        return self.__name

    pass


my_person = MyPersonAlter1("Joshua", "Sanchez")
print(MyPersonAlter1.fullname)
print(MyPersonAlter2.get_name())
MyPersonAlter1.walk()
