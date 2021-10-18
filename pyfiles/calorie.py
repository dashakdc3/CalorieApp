from .temperature import Temperature


class Calorie:
    """Represent amount of caloriies calculated with 
    BMR = 10*weight + 6.25*height - 5*age+5 - 10*temperature"""

    def __init__(self, weight, height, age, temperature):
        self.w = weight
        self.h = height
        self.a = age
        self.t = temperature

    def calculate(self):
        bmr = (10 * self.w) + (6.25 * self.h) - \
            (5 * self.a + 5) - (10 * float(self.t))
        return bmr


if __name__ == "__main__":
    temperature = Temperature(city="Minsk", country="Belarus").get()
    calorie = Calorie(weight=76, height=72, age=24, temperature=temperature)
    print(calorie.calculate())
