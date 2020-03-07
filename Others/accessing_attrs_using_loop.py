person_dict = {
    "firstname": "Brent Jeffson",
    "middlename": "Flores",
    "lastname": "Florendo",
}

class Person:
    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"
    pass

person = Person()

for key, val in person_dict.items():
    setattr(person, key, val)

for key in person_dict.keys():
    getattr(person, key)

print(person)

person2 = Person()
person2.firstname = "Brent Jeffson"

print(person2.firstname)




