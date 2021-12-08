# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

print("Coup.py")


class Player:
    def __init__(self, name):
        self.active = 0
        self.cards = []
        self.coins = 2
        self.name = str(name)
    def show(self):
        print("player " + self.name)
        print("-------",end="")
        for character in self.name:
            print("-",end="")
        print()
        if(self.active):
            print("Cards held: %d (%s)" % (len(self.cards),self.cards))
            print("Coins: %d" % (self.coins))
            print()
        else:
            print("eliminated")
            print()
            print()

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(3):
            self.cards.append("Duke")
            self.cards.append("Captain")
            self.cards.append("Ambassador")
            self.cards.append("Assassin")
            self.cards.append("Cotessa")
    def show(self):
        print("Deck")
        print("----")
        for card in self.cards:
            print(card)
        print()
    def shuffle(self):
        random.shuffle(self.cards)
    def draw(self):
        if len(self.cards) == 0:
            return None
        card = self.cards[0]
        self.cards.remove(card)
        return card


class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        for player in players:
            self.players.append(Player(player))
        for player in self.players:
            player.active = 1
            player.cards = [self.deck.draw(),self.deck.draw()]
    def show(self):
        self.deck.show()
        for player in self.players:
            player.show()


standardPlayers = ["Daniel", "Val", "Dinobytes"]
thegame = Game(standardPlayers)