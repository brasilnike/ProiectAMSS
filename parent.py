from person import Person


class Parent(Person):
    def __init__(self, first_name, last_name, age, email, phone_number, gender, responsibilities):
        super().__init__(first_name, last_name, age, email, phone_number, gender, responsibilities)

    def can_handle(self, task):
        if self.responsibilities == "Parent":
            return True
        if task.level_of_responsibility == "Parent without driving license" or task.level_of_responsibility == "Over 18 without driving license" or task.level_of_responsibility == "Kid":
            return True
        return False
