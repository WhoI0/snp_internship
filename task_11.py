class Dessert:
    def __init__(self):
        self._calories = 0
        self._name = ''

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    @name.setter
    def name(self, name):
        self._name = name

    @calories.setter
    def calories(self, calories):
        if type(calories) != int:
            raise ValueError('Калории должны быть числом')
        self._calories = calories

    def is_healthy(self):
        if self._calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True

#  Pudding = Dessert('Pudding', 300)
#  Pancake = Dessert('Pancake', 190)
#  Jelly = Dessert('Jelly', 100)
#
# print(Pudding.get_name(), Pudding.get_calories(), Pudding.is_healthy())
#
# dessert = Dessert()
# dessert.set_calories(300)
# print(dessert.is_healthy())
