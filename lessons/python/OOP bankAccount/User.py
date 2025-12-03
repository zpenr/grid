class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name and new_name.isalpha():
            self.__name = new_name
        else: raise ValueError("Некорректное имя")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0<=value<=110:
            self._age = value
        else: raise ValueError("Некорректный возраст")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self._age
    
    def set_age(self, value):
        self.age = value
