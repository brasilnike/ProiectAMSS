from abc import ABC, abstractmethod

class AbstractHuman(ABC):
    
    @abstractmethod
    def get_age_type(self):
        pass
    @abstractmethod
    def get_name(self):
        pass
    

class AdultHuman(AbstractHuman):
    
    def __init__(self,name):
        self.age = "Adult"
        self.name=name
        
    def get_age_type(self):
        return f"age Type: {self.age}"
    def get_name(self):
        return f"Name : {self.name}"
    
class ChildHuman(AbstractHuman):
    
    def __init__(self,name):
        self.age = "Child"
        self.name=name

    def get_age_type(self):
        return f"age Type: {self.age}"
    def get_name(self):
        return f"Name: {self.name}"

      
class HumanFactory():
    
    @staticmethod
    def build_Human(plan,plan_name):
        try:
            if plan == "Adult":
                return AdultHuman(plan_name)
            elif plan == "Child":
                return ChildHuman(plan_name)
            
            raise AssertionError("Human type is not valid.")
        except AssertionError as e:
            print(e) 

plan_list = [("Adult","Saul"), ("Adult","Chuck"), ("Child","Jimmy"),("Cow","Milka")]
for p in plan_list:
    Human = HumanFactory.build_Human(p[0],p[1])
    age = Human.get_age_type()
    name=Human.get_name()
    print(age,name)
