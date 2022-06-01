from modules.user import User

class House(User):
    def print_card(self):
        card_name = self.card['card']
        print(f'House card: {card_name}')

if __name__ == '__main__':
    pass