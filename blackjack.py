import random
from art import logo

def create_deck():
    """Create a standard 52-card deck for Blackjack values."""
    # 2–10: 4x každá hodnota
    deck = []
    for value in range(2, 11):
        deck.extend([value] * 4)

    # J, Q, K: 10 (4 sady každá)
    deck.extend([10] * 12)  # 3 hodnoty * 4 barvy = 12 karet

    # A: 11 (4x)
    deck.extend([11] * 4)

    random.shuffle(deck)
    return deck

def deal_card(deck):
    """Deal one card from the deck (no replacement)."""
    return deck.pop()

def calculate_score(cards):
    """ Takes a list of cards and calculates the score """
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #blackjack
    
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "You lose, computer has Blackjack!"
    elif u_score == 0:
        return "You win, you have Blackjack!"
    elif u_score > 21:
        return "You lose, you went over 21!"
    elif c_score > 21:
        return "You win, computer went over!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    print(logo)

    deck = create_deck()

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}") 
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card(deck))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand is: {user_cards}, final score: {user_score}") 
    print(f"Computer's final hand is: {computer_cards}, computer's final score is: {computer_score} ")
    print(compare(user_score, computer_score))

def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\n" * 50)
        play_game()

if __name__ == "__main__":
    main()



    





