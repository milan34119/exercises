from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def start_engine():
        ...
        
    @abstractmethod
    def stop_engine():
        ...
        
    @abstractmethod
    def drive():
        ...
        
    