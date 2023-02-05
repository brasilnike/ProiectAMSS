from abc import abstractmethod
from enum import Enum



class Person:
    @abstractmethod
    def __init__(self, first_name, last_name, age, email, phone_number, gender, responsibilities):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.responsibilities = responsibilities
        self.gender = gender
        self.age = age
    def can_handle(self, task):
        if task.level_of_responsibility == "Kid":
            return True
        return False