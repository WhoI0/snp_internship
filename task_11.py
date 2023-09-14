class Dessert:
    def __init__(self, name='', calories=0):
        self._calories = calories
        self._name = name

    def get_name(self):
        return self._name

    def get_calories(self):
        return self._calories

    def set_name(self, name):
        self._name = name

    def set_calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        if self._calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


Pudding = Dessert('Pudding', 250)
Pancake = Dessert('Pancake', 190)
Jelly = Dessert('Jelly', 100)

print(Pudding.get_name(), Pudding.get_calories(), Pudding.is_delicious())
