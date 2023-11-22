from cards import *


def play_poker():
    player_name = str(input("Enter your chosen name"))
    num_players = int(input("How many players would you like to play with? (Max 10 players)"))
    if num_players <= 10:
        players = Players(player_name, num_players)
        hands = players.get_hands()
        player_names = players.get_players()
        pre_flop = hands[player_name]
        print("Your hand:", pre_flop)
        see_flop = str(input("Continue? y/n"))
        if see_flop == 'y':
            players.flop()
            print("Flop:", players.get_comm_cards())
            see_turn = str(input("Continue? y/n"))
            if see_turn == 'y':
                players.turn()
                print("Turn:", players.get_comm_cards())
                see_river = str(input("Continue? y/n"))
                if see_river == 'y':
                    players.river()
                    print("River:", players.get_comm_cards())
                    players.winner()



#play_poker()

def rank_test():
    test = Test_Players()
    test.mult_three_of_a_kinds()
rank_test()


def hand_test():
    player_name = str(input("Enter your chosen name"))
    num_players = int(input("How many players would you like to play with? (Max 10 players)"))
    if num_players <= 10:
        players = Players(player_name, num_players)
        hands = players.get_hands()
        player_names = players.get_players()
        pre_flop = hands[player_name]
        print("Your hand:", pre_flop)
        see_flop = str(input("Continue? y/n"))
        if see_flop == 'y':
            players.flop()
            print("Flop:", players.get_comm_cards())
            see_turn = str(input("Continue? y/n"))
            if see_turn == 'y':
                players.turn()
                print("Turn:", players.get_comm_cards())
                see_river = str(input("Continue? y/n"))
                if see_river == 'y':
                    players.river()
                    print("River:", players.get_comm_cards())
                    players.mult_pairs()

#hand_test()
def large_num_test():
    count = 0
    hc = 0
    pair = 0
    pair_two = 0
    three = 0
    straight = 0
    flush = 0
    full_house = 0
    four = 0
    straight_flush = 0
    rf = 0
    while count != 10000:
        play_poker2()
        if play_poker2() == 1:
            hc += 1
        elif play_poker2() == 2:
            pair += 1
        elif play_poker2() == 3:
            pair_two += 1
        elif play_poker2() == 4:
            three += 1
        elif play_poker2() == 5:
            straight += 1
        elif play_poker2() == 6:
            flush += 1
        elif play_poker2() == 7:
            full_house += 1
        elif play_poker2() == 8:
            four += 1
        elif play_poker2() == 9:
            straight_flush += 1
        elif play_poker2() == 10:
            rf += 1
        else:
            count += 1



    print("High Cards:", hc)
    print("Pairs:", pair)
    print("Two Pairs:", pair_two)
    print("Three Of A Kinds:", three)
    print("Straights: ", straight)
    print("Flushes:", flush)
    print("Full houses:", full_house)
    print("Four Of A Kinds:", four)
    print("Straight Flushes:", straight_flush)
    print("Royal Flush:", rf)

