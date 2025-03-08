import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Want to play a blackjack game 'y', 'n': ").lower()


while True:
    if play != 'y':
        print("Bye! See you soon.")
        break

    my_cards = list(random.sample(cards, 2))
    com_cards = list(random.sample(cards, 2))
    print(f"Your cards: {my_cards}")
    print(f"One of the Computer's card is: {com_cards[0]}")

    nxt_card = input("Type, 'y' to get next card, 'r' to get result: ")

    if nxt_card == 'r':
        print(f"Your score is: {sum(my_cards)}")
        print(f"Computer's score is: {sum(com_cards)}")
        
        my_score = 21 - (int(my_cards[0]) + int(my_cards[1]))
        com_score = 21 - (int(com_cards[0]) + int(com_cards[1]))
        
        if my_score < com_score:
            print("You win. \n")
            print(f"Computer's cards is: {com_cards}")
            break
        elif my_score == com_score:
            print("Ties. \n")
            print(f"Computer's cards is: {com_cards}")
            break
        else:
            print("Computer wins.")
            break

    elif nxt_card == 'y':
        # appending one new (a1) card in player cards
        a1 = random.choice(cards)
        my_cards.append(a1)
        print(f"Your cards: {my_cards}")

        # apending one new (b1) card in computer's cards
        b1 = random.choice(cards)
        com_cards.append(b1)
        print(f"Computer's cards is: {com_cards[:-1]}")


        nxt_card = input("Type, 'y' to get next card, 'r' to get result: ")

        if nxt_card == 'r':
            my_score = 21 - (sum(my_cards))
            com_score = 21 - (sum(com_cards))

            print(f"Your score is: {sum(my_cards)}")
            print(f"Computer's score is: {sum(com_cards)}")
        
            if my_score < com_score:
                print("You win.")
                print(f"Computer's cards is: {com_cards}")
                break
            elif my_score == com_score:
                print("Ties.")
                print(f"Computer's cards is: {com_cards}")
                break
            else:
                print(f"Computer wins with cards: {com_cards}")
                break

        
            my_score = 21 - (sum(my_cards))
            com_score = 21 - (sum(com_cards))

            print(f"Your score is: {sum(my_cards)}")
            print(f"Computer's score is: {sum(com_cards)}")
            
        
            if my_score < com_score:
                print("You win.")
                print(f"Computer's cards is: {com_cards}")
                break
            else:
                print(f"Computer wins with Cards: {com_cards}")
                break
            
