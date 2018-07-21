

class Menu:
    name = None

    def __init__(self, soups, mains, discount=None):
        self._soups = soups
        self._mains = mains
        self._discount = discount

    @property
    def soups(self):
        return self._soups

    @property
    def mains(self):
        return self._mains

    @property
    def discount(self):
        return self._discount

    def __str__(self):
        return f'Soups - {self.soups}, Mains - {self.mains}, Discount - {self.discount}'


class JedalenTomiMenu(Menu):
    name = 'Stokáreň'

    def without_colon(self, s):
        splitted = s.split(':')
        if splitted == 1:
            return splitted
        splitted = splitted[1:]
        return ' '.join(splitted)

    @property
    def mains(self):
        return [self.without_colon(m) for m in self._mains]

    @property
    def discount(self):
        return self.without_colon(self._discount)
