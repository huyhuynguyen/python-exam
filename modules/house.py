from modules.user import User

class House(User):
    def print_card(self):
        print(f'House card: {self.card_name}')

# if __name__ == '__main__':
#     pass