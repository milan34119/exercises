class Duration:
    def __init__(self, *, duration_in_seconds):
        self.__duration_in_seconds = duration_in_seconds

    @property
    def seconds(self):
        return self.__duration_in_seconds

    @property
    def minutes(self):
        return self.__duration_in_seconds / 60

    @property
    def hours(self):
        return self.__duration_in_seconds / 3600
    
    @staticmethod
    def from_hours(amount):
        return Duration(duration_in_seconds=amount * 3600)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(duration_in_seconds=amount * 60)
    
    @staticmethod
    def from_seconds(amount):
        return Duration(duration_in_seconds=amount)