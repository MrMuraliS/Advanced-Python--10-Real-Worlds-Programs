from temperature import Temperature


class Calorie:
    """
    This class will calculate the calories
    that user supposed to take today
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * float(self.weight) + 6.5 * float(self.height) + 5 - float(self.temperature) * 10
        return result


# if __name__ == '__main__':
#     temperature_data = Temperature(country=input('Enter your country name: '),
#                                    city=input('Enter your city name: ')).get()
#     calorie = Calorie(temperature=temperature_data, weight=70, height=175, age=25)
#     print(calorie.calculate())
