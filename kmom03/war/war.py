#!/usr/bin/env python3

"""
Main object file
"""
from deck import Deck
from hand import Hand

class War:
    """War game"""
    def __init__(self, player1, player2):
        """init"""
        self.player1 = Hand(player1)
        self.player2 = Hand(player2)
        self.deck = Deck()
        self.pile = []

        self.split_deck()
        self.start_game()

    def get_pile(self):
        """Returns the game pile"""
        return self.pile

    def split_deck(self):
        """Splits the deck in half and shares between the two hands"""
        self.player1.set_hand(self.deck.get_deck()[ : 26])
        self.player2.set_hand(self.deck.get_deck()[26 : ])

    def start_game(self):
        """Start the game"""
        print("\nNew round :)\n")
        player1_turn = self.player1.get_player()
        player2_turn = self.player2.get_player()
        high_card_value = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

        while self.player1.get_hand() and self.player2.get_hand():
            player1_card = self.player1.get_hand().pop()
            player2_card = self.player2.get_hand().pop()

            player1_suit = player1_card.get_suit()
            player2_suit = player2_card.get_suit()

            player1_value = player1_card.get_value()
            player2_value = player2_card.get_value()

            if player1_value in high_card_value:
                player1_value = high_card_value[player1_value]

            if player2_value in high_card_value:
                player2_value = high_card_value[player2_value]

            print("{p1} draws {p1card}".format(
                p1=player1_turn,
                p1card=player1_card))

            print("{p2} draws {p2card}".format(
                p2=player2_turn,
                p2card=player2_card))

            self.pile.append(player1_card)
            self.pile.append(player2_card)

            input("Press Enter to continue...\n")

            if player1_suit == player2_suit:
                if player1_value > player2_value:
                    print("{p1} wins and picks up all the cards".format(
                        p1=player1_turn))
                    self.player1.set_hand(self.pile + self.player1.get_hand())
                else:
                    print("{p2} wins and picks up all the cards".format(
                        p2=player2_turn))
                    self.player2.set_hand(self.pile + self.player2.get_hand())
                self.pile = []
                print("Status:")
                print("{p1}: {p1cards} cards left".format(
                    p1=player1_turn, p1cards=str(len(self.player1.get_hand()))))
                print("{p2}: {p2cards} cards left".format(
                    p2=player2_turn, p2cards=str(len(self.player2.get_hand()))))
                input("Press Enter to continue...\n")

        if self.player1.get_hand() and not self.player2.get_hand():
            print("{p1} wins!".format(p1=self.player1.get_player()))
        elif self.player2.get_hand() and not self.player1.get_hand():
            print("{p2} wins!".format(p2=self.player2.get_player()))
        print("Game over!")

if __name__ == '__main__':
    new_game = War("Player 1", "Player 2")
