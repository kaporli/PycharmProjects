import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

current_score = 0
dealer_score = 0

hand = []
dealers_hand = []

first_draw = input("Do you want to play Blackjack? Type 'y' or 'n': ")

if first_draw == "n":
    print("Maybe next time then...")
elif first_draw == "y":
    dealt_hand = (random.choice(cards), 2)
    hand += dealt_hand

    dealer_score = (random.choice(cards))
    dealers_hand.append(dealer_score)

    current_score = dealt_hand[0] + dealt_hand[1]

    print(f"    Your cards are: {hand} your current score is: [{current_score}]")
    print(f"    The dealer's first card is: [{dealer_score}]")

    new_draw = input("Type 'y' to get another card, or type 'n' to pass: ")
    if new_draw == "y":
        while current_score <= 21 and new_draw == "y":
            new_card = (random.choice(cards))
            hand.append(new_card)
            current_score += new_card
            if 11 in hand and sum(hand) > 21:
                hand.remove(11)
                hand.append(1)
                current_score -= 10
            print(f"   Your cards are: {hand}. Your score is now: [{current_score}]")
            if current_score > 21:
                print("   Your score is greater than [21]. You lost.")
                break
            elif current_score == 21:
                print("   You got Blackjack. You win!")
                break
            new_draw = input("Type 'y' to draw another card, or type 'n' to pass: ")

    if new_draw == "n":
        while dealer_score < 17:
            dealers_new_card = (random.choice(cards))
            dealers_hand.append(dealers_new_card)
            dealer_score += (dealers_new_card)
            if 11 in dealers_hand and sum(dealers_hand) > 21:
                dealers_hand.remove(11)
                dealers_hand.append(1)
                dealer_score -= 10
            if dealer_score >= 17:
                print(f"   The dealer's cards are: {dealers_hand}. The dealer's score is now: [{dealer_score}]")
                break

        if dealer_score > 21:
            print("   The dealer's score is greater than [21]. You win!")
        elif dealer_score == 21:
            print("   The dealer got Blackjack. You lose.")
        elif current_score > dealer_score:
            print("   Your score is greater than the dealer's. You win!")
        elif current_score < dealer_score:
            print("   Your score is lower than the dealer's. You lose.")
        else:
            print("   You tied with the dealer. It's a draw.")