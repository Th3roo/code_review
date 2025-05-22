"""
This module defines a Card class and functions to create and manage a
standard deck of 52 playing cards. It also includes a simple example
of dealing cards to a dealer and a player.
"""

import random

SUITS = ('Пик', 'Червей', 'Бубен', 'Треф')
RANK_NAMES = (
    'Двойка', 'Тройка', 'Четвёрка', 'Пятёрка', 'Шестёрка', 'Семёрка',
    'Восьмёрка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз'
)
# Card costs: 2-10 for numbered cards, 10 for J, Q, K, 11 for Ace (can be 1 too)
# For simplicity here, Ace is 11, J,Q,K are 10.
# Adjusted costs based on typical card games (e.g., Blackjack).
# Original code had Ace as 1, then 2-9 as 2-9, 10,J,Q,K as 10.
# Let's follow a common pattern: 2-9 are their number, 10,J,Q,K are 10, Ace is 11 or 1.
# For this refactoring, let's define costs more explicitly for clarity.
# Rank order for cost calculation: 2, 3, ..., 9, 10, J, Q, K, A
# Costs: 2, 3, ..., 9, 10, 10, 10, 10, 11 (or 1 for Ace, context-dependent)

class Card:
    """
    Represents a playing card with a rank, suit, and cost.
    """
    def __init__(self, name: str, suit: str, cost: int):
        """
        Initializes a Card object.

        Args:
            name: The rank name of the card (e.g., 'Туз', 'Король').
            suit: The suit of the card (e.g., 'Пик', 'Червей').
            cost: The point value of the card.

        Raises:
            TypeError: If name or suit is not a string, or cost is not an int.
            ValueError: If suit is not a valid suit, name is not a valid rank,
                        or cost is negative.
        """
        if not isinstance(name, str):
            raise TypeError("Card name must be a string.")
        if not isinstance(suit, str):
            raise TypeError("Card suit must be a string.")
        if not isinstance(cost, int):
            raise TypeError("Card cost must be an integer.")

        if suit not in SUITS:
            raise ValueError(f"Invalid suit '{suit}'. Must be one of {SUITS}.")
        if name not in RANK_NAMES:
            raise ValueError(
                f"Invalid rank name '{name}'. Must be one of {RANK_NAMES}."
            )
        if cost < 0: # Basic cost validation, specific game rules might differ
            raise ValueError("Card cost cannot be negative.")

        self.name = name
        self.suit = suit
        self.cost = cost

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        """
        return f"{self.name} {self.suit} (Стоимость: {self.cost})"

    def __repr__(self) -> str:
        """
        Returns an official string representation of the card.
        """
        return f"Card(name='{self.name}', suit='{self.suit}', cost={self.cost})"


def get_card_cost(rank_name: str) -> int:
    """
    Determines the cost of a card based on its rank name.
    J, Q, K cost 10. Ace costs 11 (can be 1 in some games).
    Other cards cost their face value.
    """
    if rank_name in ('Валет', 'Дама', 'Король'):
        return 10
    if rank_name == 'Туз':
        return 11 # Default Ace value
    try:
        # For ranks 'Двойка' through 'Десятка'
        # This requires mapping names to values if names are not numeric strings
        rank_to_value = {
            'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4, 'Пятёрка': 5,
            'Шестёрка': 6, 'Семёрка': 7, 'Восьмёрка': 8, 'Девятка': 9,
            'Десятка': 10
        }
        return rank_to_value[rank_name]
    except KeyError:
        # Should not happen if RANK_NAMES is used for card creation
        raise ValueError(f"Unknown rank name for cost calculation: {rank_name}")


def create_deck() -> list[Card]:
    """
    Creates a standard 52-card deck.
    The deck is shuffled before being returned.

    Returns:
        A list of Card objects representing a shuffled deck.
    """
    deck = []
    for suit in SUITS:
        for rank_name in RANK_NAMES:
            cost = get_card_cost(rank_name)
            try:
                deck.append(Card(rank_name, suit, cost))
            except (TypeError, ValueError) as e:
                # This should ideally not happen if SUITS and RANK_NAMES are correct
                print(f"Error creating card {rank_name} of {suit}: {e}")
                # Optionally, re-raise or handle more gracefully
    random.shuffle(deck)
    return deck


def deal_cards(deck: list[Card], num_cards: int) -> list[Card]:
    """
    Deals a specified number of cards from the top of the deck.

    Args:
        deck: The list of Card objects (the deck).
        num_cards: The number of cards to deal.

    Returns:
        A list of Card objects dealt from the deck.

    Raises:
        ValueError: If not enough cards are in the deck or num_cards is negative.
        TypeError: If deck is not a list of Cards.
    """
    if not isinstance(deck, list) or not all(isinstance(c, Card) for c in deck):
        raise TypeError("Deck must be a list of Card objects.")
    if not isinstance(num_cards, int):
        raise TypeError("Number of cards must be an integer.")
    if num_cards < 0:
        raise ValueError("Number of cards to deal cannot be negative.")
    if num_cards > len(deck):
        raise ValueError(
            f"Not enough cards in deck to deal {num_cards}. "
            f"Deck has {len(deck)} cards."
        )
    
    dealt_cards = []
    for _ in range(num_cards):
        dealt_cards.append(deck.pop())
    return dealt_cards

# --- Main game logic example ---
if __name__ == "__main__":
    try:
        main_deck = create_deck()
        print(f"Колода создана. Количество карт: {len(main_deck)}")

        # Example: dealing 2 cards to a dealer and a player
        num_initial_cards = 2
        
        dealer_hand = deal_cards(main_deck, num_initial_cards)
        player_hand = deal_cards(main_deck, num_initial_cards)

        print(f"\nКарты Дилера ({len(dealer_hand)}):")
        for card in dealer_hand:
            print(card) # Uses Card.__str__

        print(f"\nКарты Игрока ({len(player_hand)}):")
        for card in player_hand:
            print(card) # Uses Card.__str__

        print(f"\nОставшиеся карты в колоде: {len(main_deck)}")

        # Original problematic print loop:
        # for i in range(len(Player)):
        # print(deck[i].name, deck[i].mast)
        # This was trying to access the main_deck using Player's length as index,
        # which is incorrect after cards have been popped.
        # The corrected version above prints the actual hands.

    except (ValueError, TypeError) as e:
        print(f"Произошла ошибка: {e}")
    except IndexError:
        # This might occur if pop is called on an empty deck,
        # though deal_cards should prevent this.
        print("Произошла ошибка: попытка взять карту из пустой колоды.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
