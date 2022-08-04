from traceback import format_exc


class student:
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age
    def dict(self):
        new_dict = self.__dict__
        new_dict({'__class__':self.__class__.__name__})
        return new_dict

type1 = student()
print(type1.__dict__)

    
    