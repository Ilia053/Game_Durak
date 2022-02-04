from random import choices
from random import choice
from pprint import pprint

suits_card = ['s', 'c', 'h', 'd']

values = {
    'super': 10,
    'A': 9,
    'K': 8,
    'Q': 7,
    'J': 6,
    '1': 5,
    '9': 4,
    '8': 3,
    '7': 2,
    '6': 1
}

deck_of_cards_list = ['as', 'ah', 'ac', 'ad', 'ks', 'kh', 'kc', 'kd', 'qs', 'qh', 'qc', 'qd', 'js', 'jh', 'jc', 'jd',
                      '1s', '1h', '1c', '1d', \
                      '9s', '9h', '9c', '9d', '8s', '8h', '8c', '8d', '7s', '7h', '7c', '7d', '6s', '6h', '6c', '6d']


# class Table:
#     def __init__(self,name_play,value_card, number_card, suit):
#         # self._table_game = Game(a,b,c)
#         self._table_deck = Deck_Cards(value_card, number_card, suit)
#         self._table_play_1 = Player(name_play[0])
#         self._table_play_2 = Player(name_play[1])

class Card:
    def __init__(self, name_suit, trump):
        self.name = str(name_suit.upper())[0]
        self.suit = str(name_suit.upper())[1]
        self._value = values[self.name]
        self.trump = str(trump.upper())
        if self.trump == self.suit:
            self.super_suit = True
        else:
            self.super_suit = False

    @property
    def full_name(self):
        return self.name + self.suit

    def __eq__(self, other):
        return isinstance(other, Card) and self.suit == other.suit and self.name == other.name

    def __ne__(self, other):
        if isinstance(other, Card):
            if self.suit != other.suit and self.super_suit == False and other.super_suit == False:
                return False

    def __lt__(self, other):
        if isinstance(other, Card):
            if other.super_suit and self.super_suit == False:
                return True
            if other.super_suit and self.super_suit:
                return self._value < other._value
            return self.suit == other.suit and self._value < other._value

    def __gt__(self, other):
        if isinstance(other, Card):
            if self.super_suit and other.super_suit == False:
                return True
            if self.super_suit and other.super_suit:
                return self._value > other._value
            return self.suit == other.suit and self._value > other._value


class Game:
    def __init__(self, trump):
        self.trump = trump

    #     self.first_card = Card(a, c)
    #     self.second_card = Card(b, c)
    #     print(a,b,c)

    def show_card(self):
        print(self.first_card.full_name)
        print(self.second_card.full_name)

    def start_game(self, a, b):
        # x = 0
        self.first_card = Card(a, self.trump)
        self.second_card = Card(b, self.trump)
        print(self.first_card.full_name, self.second_card.full_name, self.trump)

        if self.first_card > self.second_card:
            print('First')
        elif self.first_card < self.second_card:
            print('Second')
        elif self.first_card == self.second_card:
            print('Error')
        elif self.first_card != self.second_card:
            print('Error')
        else:
            print('something wrong!')
            return 5


class Player:
    def __init__(self, name,hand):
        self.name = name
        self.hand = hand

    @property
    def step(self):
        st = self.hand.pop()
        return str(st)

    def take_1_card(self, x):
        return self.hand.append(x)



class Deck_Cards:
    def __init__(self, value_card, number_card, suit):
        self.value_card = value_card
        self.all_card = number_card
        self.suit = suit

    @property
    def give_6_card(self):
        give = choices(self.all_card, k=6)
        self.all_card = set(self.all_card) - set(give)
        self.all_card = list(self.all_card)
        return give

    @property
    def give_1_card(self):
        if self.all_card:
            give_1 = self.all_card.pop()
            return give_1
        else:
            pass

    @property
    def joker(self):
        jok = choice(self.suit)
        return str(jok.upper())


if __name__ == '__main__':
    pprint(Deck_Cards.__dict__)
