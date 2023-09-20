class Dessert:
    def __init__(self, name='', calories=0):
        self.calories = calories
        self.name = name

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
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