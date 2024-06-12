from util import *

def group_by_suit(cards):
    return group_by(cards, lambda card : card.suit)

