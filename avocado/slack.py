import random

from slacky.attachment import SlackAttachment, AttachmentField

colors = ['#16BAC5', '#5FBFF9', '#EFE9F4', '#171D1C', '#5863F8']
veggie_e = [':avocado:', ':eggplant:', ':broccoli:', ':carrot:']
poultry_e = [':chicken:', ':poultry_leg:']
pork_e = [':pig:', ':bacon:']
beef_e = [':cow:', ':cut_of_meat:']


class MenuSlackAttachment(SlackAttachment):

    def __init__(self, menu, **kwargs):
        super().__init__(**kwargs)
        self.menu = menu

    def get_color(self):
        return random.choice(colors)

    def get_title(self):
        return self.menu.name

    def get_fields(self):
        discount = AttachmentField(':knife_fork_plate: *Menu*', f'{self.menu.discount}',
                                   short=False)

        s = '\n'.join(self.menu.soups)
        soups = AttachmentField(':soup: *Polievky*', f"{s}", short=False)

        fields = []
        for i, m in enumerate(self.menu.mains):
            e = self.pick_emoji(m)
            f = AttachmentField(f'{e} *Menu {i+1}*', m)
            fields.append(f)

        return [f.as_dict() for f in [discount, soups, *fields]]

    def pick_emoji(self, m):
        """ Pro NLP classifier. """
        if 'kura' in m:
            return random.choice(poultry_e)
        if 'brav' in m:
            return random.choice(pork_e)
        if 'hovä' in m:
            return random.choice(beef_e)
        return random.choice(veggie_e)

