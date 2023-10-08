# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date
class Person:
    def __init__(self,  name, country):
        self.name = name
        self.country = country
    def find_age(self,date_of_birth):
        self.date_of_birth = date_of_birth
        tdy = date.today()
        present_age = date.today().year - date_of_birth.year
        if tdy < date(tdy.year, self.date_of_birth.month, self.date_of_birth.day):
            return present_age - 1           
        return present_age

name = str(input(""))
country = str(input(""))
year =int(input())
month = int(input())
dat = int(input())
date_of_birth = date(year, month, dat)

per= Person( name, country)
det = Person.find_age(per, date_of_birth)  
print(det)