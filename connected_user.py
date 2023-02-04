from kid import Kid
from parent import Parent


class ConnectedUser:
    _instance = None

    def __init__(self, first_name, last_name, age, email, phone_number, gender, responsibilities):
        if self._instance is None:
            if responsibilities == "Parent":
                self._instance = Parent(first_name, last_name, age, email, phone_number, gender, responsibilities)
            else:
                self._instance = Kid(first_name, last_name, age, email, phone_number, gender, responsibilities)
        else:
            self._instance.first_name = first_name
            self._instance.last_name = last_name
            self._instance.age = age
            self._instance.email = email
            self._instance.phone_number = phone_number
            self._instance.gender = gender
            self._instance.responsibilities = responsibilities

    @classmethod
    def get_instance(cls):
        return cls._instance
