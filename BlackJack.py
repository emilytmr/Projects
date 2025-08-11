import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:

    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if start == "y":

        def deal_card():
            hand = random.choice(cards)
            return hand

        def calculate_score(hand):
            sum(hand)
            if sum(hand) == 21 and len(hand) == 2:
                return 0 #return 0 when blackjack

            elif sum(hand) > 21 and 11 in hand:
                while 11 in hand:
                    hand.remove(11)
                    hand.append(1)
            return sum(hand)



    user_cards = [deal_card(), deal_card()]  #retrieve the return value from deal cards
    computer_cards = [deal_card(), deal_card()] #retrieve the return value from deal cards
    sum_of_user = calculate_score(user_cards)
    sum_of_computer = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    if sum_of_user == 0 or sum_of_user >= 21 or sum_of_computer == 0:
        resume = False
    else:
        resume = True

    while resume:
        another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if another_card == "y":
            user_cards.append(deal_card())
            print(f"Computer's first card: {computer_cards[0]}")
            sum_of_user = calculate_score(user_cards)
            print(f"Your cards: {user_cards}")
            if len(user_cards) == 5 and sum_of_user <= 21:
                print("You win.")
                break
            elif sum_of_user > 21:
                print("You went over, you lose.")
                break
        else:

            while sum_of_computer < 21 and sum_of_computer < sum_of_user and len(computer_cards) < 5:
                computer_cards.append(deal_card())
                sum_of_computer = calculate_score(computer_cards)
            print(f"Computer's final hand: {computer_cards}")

            if sum_of_computer > 21 or sum_of_computer < sum_of_user:
                print(f"You win.")
                resume = False
            else:
                print("You lose.")
                resume = False

