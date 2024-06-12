class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.__weight_in_kg = weight_in_kg
        self.__height_in_m = height_in_m
        
    @property
    def bmi(self):
        bmi = self.__weight_in_kg / self.__height_in_m**2
        if bmi >= 25:
            return 'fat fuck'
        elif 18.5 <= bmi <= 25:
            return 'ale dan'
        else:
            return 'eet wa meer bro'