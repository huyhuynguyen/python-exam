from modules.user import User

class House(User):
    def __init__(self) -> None:
        super().__init__()
    
    def print_card(self):
        print(f'House card: {self.card_name}')