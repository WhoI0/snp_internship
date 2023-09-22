from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, name='', calories=0, flavor=''):
        super().__init__()
        self._name = name
        self._calories = calories
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False
        else:
            return True


# GreenBean = JellyBean('GreenBean', 190, 'Grass')
# BlackBean = JellyBean('BlackBean', 185, 'black licorice')
# WhiteBean = JellyBean('WhiteBean', 215, 'Strawberry')
# print(BlackBean.get_name(), BlackBean.get_calories(), BlackBean.get_flavor(), BlackBean.is_delicious())
# print(WhiteBean.get_name(), WhiteBean.get_calories(), WhiteBean.get_flavor(), WhiteBean.is_delicious())
