from random import choices
from Classes import *

deck = Deck_Cards(values, deck_of_cards_list, suits_card)
ilia = Player('ilia', deck.give_6_card)
sveta = Player('sveta', deck.give_6_card)
# ilia = Player('ilia')
# sveta = Player('sveta')
toy = Game(deck.joker)
print(ilia.hand)
print(sveta.hand)
x = ilia.step
y = sveta.step

if toy.start_game(x, y) == 5:
    print('Card back', x)
    ilia.take_1_card(x)
    sveta.take_1_card(y)

print(ilia.hand)
print(sveta.hand)

# ilia.take_1_card_from_deck(deck.give_1_card)
