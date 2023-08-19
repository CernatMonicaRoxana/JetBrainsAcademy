import random


class Game:

    def __init__(self):
        self.default_hand = ['rock', 'paper', 'scissors']
        self.computer_hand = None
        self.hand = None
        self.cards = None
        self.points = None
        self.name = ''
        self.commands = ['!rating']

    def hello(self):
        self.name = input("Enter your name: ")
        print(f'Hello, {self.name}')

    def check_ratings_file(self):
        with open('rating.txt', 'r') as ratings:
            for line in ratings:
                name, score = line.split(" ")
                if self.name == name:
                    self.points = int(score)
                    break
                self.points = 0

    def read_hand(self):
        cards = input().split(",")
        if cards[0] == '':
            self.cards = self.default_hand
        else:
            self.cards = cards
        print("Okay, let's start")

    def winner(self):
        player_hand_idx = self.cards.index(f'{self.hand}')
        computer_hand_idx = self.cards.index(f'{self.computer_hand}')

        if player_hand_idx == computer_hand_idx:
            self.points += 50
            return f'There is a draw: ({self.cards[player_hand_idx]})'

        cards_list_len = len(self.cards)
        copy_of_cads = self.cards[player_hand_idx + 1:cards_list_len] + self.cards[:player_hand_idx]

        first_half_copy_list = copy_of_cads[0:cards_list_len // 2]
        second_half_copy_list = copy_of_cads[cards_list_len // 2:cards_list_len]

        if self.cards[computer_hand_idx] in first_half_copy_list:
            return f'Sorry, but the computer chose {self.cards[computer_hand_idx]}'
        else:
            self.points += 100
            return f'Well done. The computer chose {self.cards[computer_hand_idx]} and failed'

    def computer_choice(self):
        self.computer_hand = self.cards[random.randint(0, len(self.cards) - 1)]
        # print(self.computer_hand)
        return self.computer_hand

    def game(self):
        hands = self.cards
        commands = self.commands
        self.hand = input()

        while self.hand != '!exit':
            if (self.hand not in hands) and (self.hand not in commands):
                print('Invalid input')
                self.hand = input()
            elif self.hand == commands[0]:
                print(f'Your rating: {self.points}')
                self.hand = input()
            else:
                computer_hand = self.computer_choice()
                print(self.winner())
                self.hand = input()

    def setup(self):
        self.hello()
        self.read_hand()
        self.check_ratings_file()


if __name__ == '__main__':
    game = Game()
    game.setup()
    game.game()
