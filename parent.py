from person import Person


class Parent(Person):
    def __init__(self, first_name, last_name, age, email, phone_number, gender, responsibilities):
        super().__init__(first_name, last_name, age, email, phone_number, gender, responsibilities)

    #def can_handle(self, task):
    #    pass
    # aici o sa verifice task-ul pentru cine e pus, si vede daca persoana de fata poate sau
    # nu sa faca acel task