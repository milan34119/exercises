from abc import ABC, abstractmethod
import re

class Persoon:
    @staticmethod
    def is_valid_name(name):
        return (re.fullmatch(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', name))
        
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.__name = name
        self.is_a_student = is_a_student
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if self.is_valid_name(value):
            self.__name = value
        else:
            raise ValueError('geen naam')
        
class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}
        
    @property
    def occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        return min(self.area //20, self.number_of_rooms * 2)
    
    def register_resident(self, person):
        if isinstance(person, Persoon):
            if person.id in self.__occupants or self.occupants >= self.maximum_occupants:
                raise RuntimeError('gaatem ni worde')
            self.__occupants[id] = person
        else:
            raise RuntimeError('is geen Persoon instance g')
    
    def unregister_resident(self, id):
        if id in self.__occupants.keys:
            del self.__occupants[id]
            
    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
    
    @abstractmethod
    def calculate_value(self):
        pass
        # IK heb geen flauw idee waik hier hoor te doen??

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity
        
    def calculate_value(self):
        return ((25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity))
    
class StudentKot(Residence):
    def __init__(self, address, area):
        super.__init__(address, area, 1)

    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError('enkel studenten')
        super().register_resident(person) 
        
    def calculate_value(self):
        return 150000 + (750 * self.area)   
    