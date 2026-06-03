import random
import art
def play_game():
    print(art.logo)
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(u_score, c_score):
        """Compares the user score u_score against the computer score c_score."""
        if u_score == c_score:
            return "Draw 🙃"
        elif c_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif u_score == 0:
            return "Win with a Blackjack 😎"
        elif u_score > 21:
            return "You went over. You lose 😭"
        elif c_score > 21:
            return "Opponent went over. You win 😁"
        elif u_score > c_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    user_cards = []
    comp_cards = []
    comp_score = -1
    user_score = -1
    game_play = False

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_play:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, Your score: {user_score}")
        print(f"Computer cards: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_play = True
        else:
            draw_another_card = input("Want to draw another card type 'y' or 'n' to pass: ")
            if draw_another_card == 'y':
                user_cards.append(deal_card())

            else:
                game_play = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(compare(user_score, comp_score))
    print(f"user : {user_cards}, {user_score}")
    print(f"Comp : {comp_cards},{comp_score} ")
    while input("Do u want to play game of Blackjack 'y' or 'n': ") == 'y':
        print("\n" * 20)
        play_game()
play_game()









