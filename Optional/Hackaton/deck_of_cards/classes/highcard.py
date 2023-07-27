from .deck import Deck


class HighCardWinsGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player1_name = input("Ingrese el nombre del Jugador 1: ")
        self.player2_name = input("Ingrese el nombre del Jugador 2: ")

        self.player1_card = None
        self.player2_card = None

    def play_round(self):
        self.player1_card = self.deck.deal_card()
        self.player2_card = self.deck.deal_card()

        print(f"{self.player1_name} juega {self.player1_card.string_val} of {self.player1_card.suit}")
        print(f"{self.player2_name} juega {self.player2_card.string_val} of {self.player2_card.suit}")

        if self.player1_card.point_val > self.player2_card.point_val:
            print(f"{self.player1_name} gana la ronda!")
        elif self.player2_card.point_val > self.player1_card.point_val:
            print(f"{self.player2_name} gana la ronda!")
        else:
            print("¡Empate!")