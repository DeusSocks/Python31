import time

class Car():
    def drive(self):
        pass
    
    def stop(self):
        pass

class Animal():
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color
        
    def eat(self):
        pass
    
    def sleep(self):
        time.sleep(2)
        print(f'{self.name} поспал')

class Marker():
    def __init__(self, color) -> None:
        self.color = color
    
    def write(self, word):
        return f'Я написал {word} {self.color} маркером'

dog = Animal('Nikita', 26, 'blue')
cat = Animal('Stas', 15, 'orange')

"""print(dog.name)
dog.name = 'Ne Nikita'"""

"""marker_red = Marker('красным')
marker_blue = Marker('синим')

print(marker_red.write('пират'))"""


class User():
    def __init__(self, login, password) -> None:
        if len(login) > 4 and len(password) > 4:
            self.login = login
            self.password = password
        else:
            print('Недопустимая длина логина или пароля')
    
    def get_login(self):
        return self.login
    def get_password(self):
        return self.password
    def change_login(self, new_login):
        if len(new_login) > 4:
            self.login = new_login
        else:
            print('Недопустимая длина логина')
        return self.login
    def change_password(self, new_password):
        if len(new_password) > 4:
            self.password = new_password
        else:
            print('Недопустимая длина пароля')
        return self.password


class Human():
    def __init__(self, last_name=None, first_name=None, father_name=None, year=None, phone=None, town=None, country=None, adress=None) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.father_name = father_name
        self.year = year
        self.phone = phone
        self.town = town
        self.country = country
        self.adress = adress
    def create(self):
        self.last_name = input("Last name: ")
        self.first_name = input("First name: ")
        self.father_name = input("Father name: ")
        self.year = input("Year of born: ")
        self.phone = input("Contact phone: ")
        self.town = input("Town: ")
        self.country = input("Country: ")
        self.adress = input("Adress: ")
    def get_all(self):
        return self.last_name, self.first_name, self.father_name, self.year, self.phone, self.town, self.country, self.adress
    def get(self, property):
        return eval(f"self.{property}")
    

class Fraction():
    def __init__(self, num=None, denum=None) -> None:
        self.num:int = num
        self.denum:int = denum
    def get(self):
        return self.num, self.denum
    def get_num(self):
        return self.num
    def get_denum(self):
        return self.denum
    def sum(self, frac2):
        new_num = self.num * frac2.get_denum() + frac2.get_num() * self.denum
        new_denum = self.denum * frac2.get_denum()
        return new_num, new_denum
    def minus(self, frac2):
        new_num = self.num * frac2.get_denum() - frac2.get_num() * self.denum
        new_denum = self.denum * frac2.get_denum()
        return new_num, new_denum
    
    
    