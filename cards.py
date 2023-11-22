
import random

class Card:
    """A playing card."""

    def __init__(self, rank, suit):
        """Creates a new instance of a playing card."""
        self._rank = rank
        self._suit = suit

    def get_value(self):
        """Returns the numerical value of the card."""
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '10': 10,
                  'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return values[self._rank]

    def get_suit(self):
        return self._suit

    def __repr__(self):
        """Returns a string representation of the card."""
        suit_symbol = {'hearts': chr(9829),
                       'diamonds': chr(9830),
                       'clubs': chr(9827),
                       'spades': chr(9824)}
        return self._rank + suit_symbol[self._suit]
    

class Hand:
    """A hand of playing cards."""

    def __init__(self, starting_cards):
        """Creates a hand of playing cards."""
        self._cards = starting_cards

    def get_cards(self):
        """Returns a list of the cards in the hand."""
        return self._cards
    
    def add_hand(self, hand):
        """adds another hand to the hand"""
        for card in hand.get_cards():
            self._cards.append(card)

    def add(self, card):
        """Adds another card to the hand."""
        self._cards.append(card)

    def value(self):
        """Returns the numeric total of the cards in the hand."""
        total = 0
        for card in self._cards:
            total += card.get_value()
        return total
    
    def __repr__(self):
        """Returns a string representation of the hand."""
        card_strs = []
        for card in self._cards:
            card_strs.append(str(card))
        return " ".join(card_strs)
    

    def __iadd__(self, other):
        self._cards = Hand(self._cards + [other])
        return self._cards
    
    def __add__(self, other):
        return Hand(self._cards + [other])

    def get_ranks(self):
        ranks_of_hand = []
        for card in self.get_cards():
            ranks_of_hand += [Card.get_value(card)]
        return ranks_of_hand
    

    def is_high_card(self):
        if len(set(self.get_ranks())) == 7 and not self.is_straight() and not self.is_flush():
            return True
        else:
            return False

    
    def is_pair(self):
        ranks = self.get_ranks()
        num_pairs = 0
        for value in list(set(ranks)):
            if ranks.count(value) == 2:
                num_pairs +=1
        if num_pairs == 1:
            return True
        else:
            return False
        


    def is_two_pair(self):
        ranks = self.get_ranks()
        num_pairs = 0
        for value in list(set(ranks)):
            if ranks.count(value) == 2:
                num_pairs +=1
        if num_pairs >= 2:
            return True
        else:
            return False


    
    def is_three_of_a_kind(self):
        ranks = self.get_ranks()
        num_three_of_kind = 0
        for value in list(set(ranks)):
            if ranks.count(value) == 3:
                num_three_of_kind +=1
        if num_three_of_kind == 1:
            return True
        else:
            return False

    

    def is_straight(self):
        ranks_sorted = sorted(list(set(self.get_ranks())))
        if ranks_sorted[-1] == 14 and ranks_sorted[:4] == [2, 3, 4, 5]:
            return True
        num_consecutive = 0
        for i in range(len(ranks_sorted)):
            if i != range(len(ranks_sorted))[-1]:
                if ranks_sorted[i] + 1 == ranks_sorted[i + 1]:
                    num_consecutive += 1
                    if num_consecutive >= 4:
                        return True

                else:
                    num_consecutive = 0
        else:
            return False
       
            
    
    def is_flush(self):
        num_clubs = 0
        num_hearts = 0
        num_diamonds = 0
        num_spades = 0
        for card in self.get_cards():
            if Card.get_suit(card) == "clubs":
                num_clubs += 1
            elif Card.get_suit(card) == "hearts":
                num_hearts += 1
            elif Card.get_suit(card) == "diamonds":
                num_diamonds += 1
            elif Card.get_suit(card) == "spades":
                num_spades += 1
        if num_spades >= 5 or num_clubs >= 5 or num_hearts >= 5 or num_diamonds >= 5:
            return True
        else:
            return False

    
    def is_full_house(self):
        num_pairs = 0
        num_three_of_kinds = 0
        ranks = self.get_ranks()
        ranks_set_list = list(set(ranks))
        for value in ranks_set_list:
            if ranks.count(value) == 2:
                num_pairs +=1
            if ranks.count(value) == 3:
                num_three_of_kinds += 1
        if num_pairs >= 1 and num_three_of_kinds == 1:
            return True
        elif num_three_of_kinds == 2:
            return True
        else:
            return False

            
    def is_four_of_a_kind(self):
        ranks = self.get_ranks()
        ranks_set_list = list(set(self.get_ranks()))
        for value in ranks_set_list:
            if ranks.count(value) == 4:
                return True
        return False



    def is_straight_flush(self):
        copy_var = self
        copy_var_list = copy_var.get_cards()
        if self.is_straight() and self.is_flush():
            flush_count = {'clubs': 0, 'hearts': 0, 'diamonds': 0, 'spades': 0}
            for card in self.get_cards():
                if Card.get_suit(card) == "clubs":
                    flush_count['clubs'] += 1
                if Card.get_suit(card) == "hearts":
                    flush_count['hearts'] += 1
                if Card.get_suit(card) == "diamonds":
                    flush_count['diamonds'] += 1
                if Card.get_suit(card) == "spades":
                    flush_count['spades'] += 1
            for suit in flush_count:
                if flush_count[suit] >= 5:
                    for card in copy_var_list:
                        if Card.get_suit(card) != suit:
                            copy_var_list.remove(card)
            if copy_var.is_straight():
                return True
            else:
                return False

    def is_royal_flush(self):
        ranks = list(set(self.get_ranks()))
        if self.is_straight_flush():
            if ranks[-1:-6:-1] == [14, 13, 12, 11, 10]:
                return True
            else:
                return False
        

    def rank(self):
        value_of_hand = 1
        type_of_hand = 'High Card'
        if self.is_pair():
            type_of_hand = "Pair"
            value_of_hand = 2
        if self.is_two_pair():
            type_of_hand = "Two Pair"
            value_of_hand = 3
        if self.is_three_of_a_kind():
            type_of_hand = "Three Of A Kind"
            value_of_hand = 4
        if self.is_straight():
            type_of_hand = "Straight"
            value_of_hand = 5
        if self.is_flush():
            type_of_hand = "Flush"
            value_of_hand = 6
        if self.is_full_house():
            type_of_hand = "Full House"
            value_of_hand = 7
        if self.is_four_of_a_kind():
            type_of_hand = "Four Of A Kind"
            value_of_hand = 8
        if self.is_straight_flush():
            type_of_hand = "Straight Flush"
            value_of_hand = 9
        if self.is_royal_flush():
            type_of_hand = "Royal Flush"
            value_of_hand = 10
        #print(type_of_hand)
        return value_of_hand
    
    def type(self):
        value_of_hand = 1
        type_of_hand = 'High Card'
        if self.is_pair():
            type_of_hand = "Pair"
            value_of_hand = 2
        if self.is_two_pair():
            type_of_hand = "Two Pair"
            value_of_hand = 3
        if self.is_three_of_a_kind():
            type_of_hand = "Three Of A Kind"
            value_of_hand = 4
        if self.is_straight():
            type_of_hand = "Straight"
            value_of_hand = 5
        if self.is_flush():
            type_of_hand = "Flush"
            value_of_hand = 6
        if self.is_full_house():
            type_of_hand = "Full House"
            value_of_hand = 7
        if self.is_four_of_a_kind():
            type_of_hand = "Four Of A Kind"
            value_of_hand = 8
        if self.is_straight_flush():
            type_of_hand = "Straight Flush"
            value_of_hand = 9
        if self.is_royal_flush():
            type_of_hand = "Royal Flush"
            value_of_hand = 10
        #print(type_of_hand)
        return type_of_hand
            
    
    

class Deck:
    """A deck of cards."""

    def __init__(self):
        """Creates a new instance of a deck of playing cards."""
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'J', 'Q', 'K', 'A']
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self._cards = []
        for rank in ranks:
            for suit in suits:
                new_card = Card(rank, suit)
                self._cards.append(new_card)

    def shuffle(self):
        """Shuffles the cards of the deck."""
        from random import shuffle
        shuffle(self._cards)

    def deal(self, num_cards):
        """Deals a hand with the specified number of cards."""
        hand = Hand(self._cards[:num_cards])
        self._cards = self._cards[num_cards:]
        self._hand_list = self._cards[:num_cards]
        return hand


    def draw(self):
        """Draws a single card from the deck."""
        card = self._cards[0]
        self._cards = self._cards[1:]
        return card


class Test_Deck:
    def __init__(self):
        """Creates a new instance of a deck of playing cards."""
        ranks = ['2']
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        self._cards = []
        for rank in ranks:
            for suit in suits:
                new_card = Card(rank, suit)
                self._cards.append(new_card)



    def deal(self, num_cards):
        """Deals a hand with the specified number of cards."""
        hand = Hand(self._cards[:num_cards])
        self._cards = self._cards[num_cards:]
        self._hand_list = self._cards[:num_cards]
        return hand


class Players:
    

    def __init__(self, player_name, num_players):
        self._num_players = num_players
        self._name = player_name

        names = ["Aisling", "Aisha", "Akari", "Alessia", "Amara", "Amirah", "Ananya", "Astrid", "Bastien", "Dante",
    "Eleni", "Elio", "Esmeralda", "Fabien", "Henrik", "Ingrid", "Isidro", "Jelena", "Jiaying", "Katarina",
    "Kieran", "Levente", "Li Wei", "Lucia", "Luka", "Malina", "Mateo", "Milena", "Nika", "Rafaela",
    "Rasmus", "Renata", "Soren", "Svetlana", "Takumi", "Tariq", "Thiago", "Viktor", "Yukihiro"]

        player_dictionary = {}
        player_scores = {}
        self._deck = Deck()
        self._deck.shuffle()
        player_dictionary[player_name] = self._deck.deal(2)
        player_scores[player_name] = 0
        #while loop creating players depending on the number of players
        self._players = [player_name]
        for name in range(self._num_players):
            rand_num = random.randint(0, 29)
            name = names[rand_num]
            names.remove(names[rand_num])
            self._players += [name]
        for player in self._players:
            player_dictionary[player] = self._deck.deal(2)
            player_scores[player] = 0
        self._hands = player_dictionary
        self._scores = player_scores


    def get_hands(self):
        return self._hands
    

    def get_players(self):
        return self._players
    

    def flop(self):
        self._comm_cards = self._deck.deal(3)
        for player in self._players:
            Hand.add_hand(self._hands[player], self._comm_cards)
    

    def get_comm_cards(self):
        return self._comm_cards


    def turn(self):
        turn_card = self._deck.draw()
        for player in self._players:
            Hand.add(self._hands[player], turn_card)
        Hand.add(self._comm_cards, turn_card)


    def river(self):
        river_card = self._deck.draw()
        for player in self._players:
            Hand.add(self._hands[player], river_card)
        Hand.add(self._comm_cards, river_card)


    def better_hand(self):
        print(self._players)
        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        print(self._hands)
        each_score = sorted(each_score)
        if each_score[-1] > each_score [-2]:
            winning_score = each_score[-1]
            for player in self._scores:
                if self._scores[player] == winning_score:
                    player_cards = Hand.get_cards(self._hands[player])[:2]
                    player_cards[0] = Card.__repr__(player_cards[0])
                    player_cards[1] = Card.__repr__(player_cards[1])
                    print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                    return True


    def mult_high_cards(self):
        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        if each_score[-1] > each_score [-2]:
            winning_score = each_score[-1]
            for player in self._scores:
                if self._scores[player] == winning_score:
                    player_cards = Hand.get_cards(self._hands[player])[:2]
                    player_cards[0] = Card.__repr__(player_cards[0])
                    player_cards[1] = Card.__repr__(player_cards[1])
                    print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
        else:
            winning_hand_rank = each_score[-1]
            if winning_hand_rank:
                high_cards = []
                for player in self._scores:
                    hand = Hand.get_cards(self._hands[player])
                    for card in hand:
                        value = Card.get_value(card)
                        high_cards += [value]
                    high_cards = sorted(high_cards)
                    self._scores[player] = high_cards[-1]
                if high_cards[-1] > high_cards[-2]:
                    winning_score = high_cards[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                else:
                    high_cards = []
                    for player in self._scores:
                        hand = Hand.get_cards(self._hands[player])
                        for card in hand:
                            value = Card.get_value(card)
                            high_cards += [value]
                        high_cards = sorted(high_cards)
                        self._scores[player] = high_cards[-2]
                    if high_cards[-2] > high_cards[-3]:
                        winning_score = high_cards[-2]
                        for player in self._scores:
                            if self._scores[player] == winning_score:
                                player_cards = Hand.get_cards(self._hands[player])[:2]
                                player_cards[0] = Card.__repr__(player_cards[0])
                                player_cards[1] = Card.__repr__(player_cards[1])
                                print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                    else:
                        high_cards = []
                        for player in self._scores:
                            hand = Hand.get_cards(self._hands[player])
                            for card in hand:
                                value = Card.get_value(card)
                                high_cards += [value]
                            high_cards = sorted(high_cards)
                            self._scores[player] = high_cards[-3]
                        if high_cards[-3] > high_cards[-4]:
                            winning_score = high_cards[-3]
                            for player in self._scores:
                                if self._scores[player] == winning_score:
                                    player_cards = Hand.get_cards(self._hands[player])[:2]
                                    player_cards[0] = Card.__repr__(player_cards[0])
                                    player_cards[1] = Card.__repr__(player_cards[1])
                                    print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        else:
                            high_cards = []
                            for player in self._scores:
                                hand = Hand.get_cards(self._hands[player])
                                for card in hand:
                                    value = Card.get_value(card)
                                    high_cards += [value]
                                high_cards = sorted(high_cards)
                                self._scores[player] = high_cards[-3]
                            if high_cards[-4] > high_cards[-5]:
                                winning_score = high_cards[-4]
                                for player in self._scores:
                                    if self._scores[player] == winning_score:
                                        player_cards = Hand.get_cards(self._hands[player])[:2]
                                        player_cards[0] = Card.__repr__(player_cards[0])
                                        player_cards[1] = Card.__repr__(player_cards[1])
                                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                            else:
                                high_cards = []
                                for player in self._scores:
                                    hand = Hand.get_cards(self._hands[player])
                                    for card in hand:
                                        value = Card.get_value(card)
                                        high_cards += [value]
                                    high_cards = sorted(high_cards)
                                    self._scores[player] = high_cards[-5]
                                    winning_score = high_cards[-5]
                                    for player in self._scores:
                                        if self._scores[player] == winning_score:
                                            player_cards = Hand.get_cards(self._hands[player])[:2]
                                            player_cards[0] = Card.__repr__(player_cards[0])
                                            player_cards[1] = Card.__repr__(player_cards[1])
                                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                                        else:
                                            winning_players = []
                                            for player in self._scores:
                                                if self._scores[player] == winning_score:
                                                    winning_players += [player]
                                                winning_hands = []
                                            for player in winning_players:
                                                winning_hands += [self._hands[player]]
                                            print(','.join(winning_players) + 'All won with: ', ",".join(winning_hands))


    def mult_pairs(self):
        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        if each_score[-1] == 2 and each_score[-2] == 2:
            pair_ranks = []
            for player in self._players:
                ranks = Hand.get_ranks(self._hands[player])
                for value in list(set(ranks)):
                    if ranks.count(value) == 2:
                        pair_ranks += [value]
                        self._scores[player] = value
            pair_ranks = sorted(pair_ranks)
            if pair_ranks[-1] > pair_ranks[-2]:
                winning_score = pair_ranks[-1]
                for player in self._scores:
                    if self._scores[player] == winning_score:
                        player_cards = Hand.get_cards(self._hands[player])[:2]
                        player_cards[0] = Card.__repr__(player_cards[0])
                        player_cards[1] = Card.__repr__(player_cards[1])
                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        print(self._hands)
            else:
                pair_rank = pair_ranks[-1]
                high_cards = []
                for player in self._scores:
                    player_high_cards = []
                    hand = Hand.get_cards(self._hands[player])
                    for card in hand:
                        value = Card.get_value(card)
                        if value != pair_rank:
                            high_cards += [value]
                            player_high_cards += [value]
                        player_high_cards = sorted(player_high_cards)
                    self._scores[player] = player_high_cards[-1]
                high_cards = sorted(high_cards)
                if high_cards[-1] > high_cards[-2]:
                    winning_score = high_cards[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                else:
                    past_high_card = high_cards[-1]
                    high_cards = []
                    for player in self._scores:
                        player_high_cards = []
                        hand = Hand.get_cards(self._hands[player])
                        for card in hand:
                            value = Card.get_value(card)
                            if value != pair_rank and value != past_high_card:
                                high_cards += [value]
                                player_high_cards += [value]
                        player_high_cards = sorted(player_high_cards)
                        self._scores[player] = player_high_cards[-1]
                    high_cards = sorted(high_cards)
                    if high_cards[-1] > high_cards[-2]:
                        #print(high_cards)
                        winning_score = high_cards[-1]
                        #print(winning_score)
                        for player in self._scores:
                            if self._scores[player] == winning_score:
                                player_cards = Hand.get_cards(self._hands[player])[:2]
                                player_cards[0] = Card.__repr__(player_cards[0])
                                player_cards[1] = Card.__repr__(player_cards[1])
                                print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                    else:
                        past_high_card2 = high_cards[-1]
                        high_cards = []
                        for player in self._scores:
                            player_high_cards = []
                            hand = Hand.get_cards(self._hands[player])
                            for card in hand:
                                value = Card.get_value(card)
                                if value != pair_rank and value != past_high_card and value != past_high_card2:
                                    high_cards += [value]
                                    player_high_cards += [value]
                            player_high_cards = sorted(player_high_cards)
                            self._scores[player] = player_high_cards[-1]
                        high_cards = sorted(high_cards)
                        if high_cards[-1] > high_cards[-2]:
                            print(high_cards)
                            winning_score = high_cards[-1]
                            for player in self._scores:
                                if self._scores[player] == winning_score:
                                    player_cards = Hand.get_cards(self._hands[player])[:2]
                                    player_cards[0] = Card.__repr__(player_cards[0])
                                    player_cards[1] = Card.__repr__(player_cards[1])
                                    print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        else:
                            winning_score = high_cards[-1]
                            winning_players = []
                            winning_hands = []
                            player_cards = []
                            for player in self._scores:
                                if self._scores[player] == winning_score:
                                    winning_players += [player]
                                    winning_hands += [self._hands[player]]
                                player_cards1 = Hand.get_cards(self._hands[player])[:2]
                                player_cards1[0] = Card.__repr__(player_cards1[0])
                                player_cards1[1] = Card.__repr__(player_cards1[1])
                                player_cards += player_cards1
                            print(winning_hands)
                            print(', '.join(winning_players) + ' tied to win with :', ' '.join(player_cards))


    def mult_two_pairs(self):
        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        if each_score[-1] == 3 and each_score[-2] == 3:
            pair_ranks = []
            for player in self._players:
                ranks = Hand.get_ranks(self._hands[player])
                for value in list(set(ranks)):
                    if ranks.count(value) == 2:
                        pair_ranks += [value]
                        self._scores[player] = value
            pair_ranks = sorted(pair_ranks)
            if pair_ranks[-1] > pair_ranks[-2]:
                winning_score = pair_ranks[-1]
                for player in self._scores:
                    if self._scores[player] == winning_score:
                        player_cards = Hand.get_cards(self._hands[player])[:2]
                        player_cards[0] = Card.__repr__(player_cards[0])
                        player_cards[1] = Card.__repr__(player_cards[1])
                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        print(self._hands)
            else:
                high_pair = pair_ranks[-1]     
                pair_ranks = []
                for player in self._players:
                    ranks = Hand.get_ranks(self._hands[player])
                    for value in list(set(ranks)):
                        if ranks.count(value) == 2 and value != high_pair:
                            pair_ranks += [value]
                            self._scores[player] = value
                pair_ranks = sorted(pair_ranks)
                if pair_ranks[-1] > pair_ranks[-2]:
                    winning_score = pair_ranks[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                            print(self._hands)
                else:
                    high_pair2 = pair_ranks[-1]     
                    pair_ranks = []
                    for player in self._players:
                        ranks = Hand.get_ranks(self._hands[player])
                        for value in list(set(ranks)):
                            if value != high_pair and value != high_pair2:
                                pair_ranks += [value]
                                self._scores[player] = value
                    pair_ranks = sorted(pair_ranks)
                    if pair_ranks[-1] > pair_ranks[-2]:
                        winning_score = pair_ranks[-1]
                        for player in self._scores:
                            if self._scores[player] == winning_score:
                                player_cards = Hand.get_cards(self._hands[player])[:2]
                                player_cards[0] = Card.__repr__(player_cards[0])
                                player_cards[1] = Card.__repr__(player_cards[1])
                                print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                                print(self._hands)
                    else:
                        winning_score = pair_ranks[0]
                        winning_players = []
                        winning_hands = []
                        player_cards = []
                        for player in self._scores:
                            winning_players += [player]
                            winning_hands += [self._hands[player]]
                            player_cards1 = Hand.get_cards(self._hands[player])[:2]
                            player_cards1[0] = Card.__repr__(player_cards1[0])
                            player_cards1[1] = Card.__repr__(player_cards1[1])
                            player_cards += player_cards1
                        print(winning_hands)
                        print(', '.join(winning_players) + ' all tied to win with :', ' '.join(player_cards))


    def mult_three_of_a_kinds(self):

        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        print(each_score)
        if each_score[-1] == 4 and each_score[-2] == 4:
            pass
    

    def mult_straights(self):
        pass


    def mult_flushes(self):
        pass


    def mult_full_houses(self):
        pass


    def mult_four_of_a_kinds(self):
        pass


    def mult_straight_flushes(self):
        pass


class Test_Players:


    def __init__(self):


        player_dictionary = {}
        player_scores = {}
        self._deck = Test_Deck()
        self._players = ['player1', 'player2']
        hand = self._deck.deal(1)
        card1 = Card('A', "spades")
        card2 = Card('5', "diamonds")
        card3 = Card('4', "hearts")
        card4 = Card('2', 'clubs')
        card5 = Card('7', 'spades')
        card6 = Card('2', 'diamonds')
        Hand.add(hand,card1)
        Hand.add(hand,card2)
        Hand.add(hand,card3)
        Hand.add(hand,card4)
        Hand.add(hand,card5)
        Hand.add(hand,card6)
        player_dictionary['player1'] = hand
        player_scores['player1'] = 0
        hand2 = self._deck.deal(1)
        card1 = Card('A', "diamonds")
        card2 = Card('3', "diamonds")
        card3 = Card('4', "hearts")
        card4 = Card('2', 'clubs')
        card5 = Card('7', 'spades')
        card6 = Card('2', 'diamonds')
        Hand.add(hand2,card1)
        Hand.add(hand2,card2)
        Hand.add(hand2,card3)
        Hand.add(hand2,card4)
        Hand.add(hand2,card5)
        Hand.add(hand2,card6)
        player_dictionary['player2'] = hand2
        self._hands = player_dictionary
        self._scores = player_scores



    def mult_pairs(self):
        print(self._hands)
        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        if each_score[-1] == 2 and each_score[-2] == 2:
            pair_ranks = []
            for player in self._players:
                ranks = Hand.get_ranks(self._hands[player])
                for value in list(set(ranks)):
                    if ranks.count(value) == 2:
                        pair_ranks += [value]
                        self._scores[player] = value
            if pair_ranks[-1] > pair_ranks[-2]:
                winning_score = pair_ranks[-1]
                for player in self._scores:
                    if self._scores[player] == winning_score:
                        player_cards = Hand.get_cards(self._hands[player])[:2]
                        player_cards[0] = Card.__repr__(player_cards[0])
                        player_cards[1] = Card.__repr__(player_cards[1])
                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        print(self._hands)
            else:
                pair_rank = pair_ranks[-1]
                high_cards = []
                for player in self._scores:
                    player_high_cards = []
                    hand = Hand.get_cards(self._hands[player])
                    for card in hand:
                        value = Card.get_value(card)
                        if value != pair_rank:
                            high_cards += [value]
                            player_high_cards += [value]
                        player_high_cards = sorted(player_high_cards)
                    self._scores[player] = player_high_cards[-1]
                high_cards = sorted(high_cards)
                if high_cards[-1] > high_cards[-2]:
                    winning_score = high_cards[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                else:
                    past_high_card = high_cards[-1]
                    high_cards = []
                    for player in self._scores:
                        player_high_cards = []
                        hand = Hand.get_cards(self._hands[player])
                        for card in hand:
                            value = Card.get_value(card)
                            if value != pair_rank and value != past_high_card:
                                high_cards += [value]
                                player_high_cards += [value]
                        player_high_cards = sorted(player_high_cards)
                        self._scores[player] = player_high_cards[-1]
                    high_cards = sorted(high_cards)
                    if high_cards[-1] > high_cards[-2]:
                        #print(high_cards)
                        winning_score = high_cards[-1]
                        #print(winning_score)
                        for player in self._scores:
                            if self._scores[player] == winning_score:
                                player_cards = Hand.get_cards(self._hands[player])[:2]
                                player_cards[0] = Card.__repr__(player_cards[0])
                                player_cards[1] = Card.__repr__(player_cards[1])
                                print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                    else:
                        past_high_card2 = high_cards[-1]
                        high_cards = []
                        for player in self._scores:
                            player_high_cards = []
                            hand = Hand.get_cards(self._hands[player])
                            for card in hand:
                                value = Card.get_value(card)
                                if value != pair_rank and value != past_high_card and value != past_high_card2:
                                    high_cards += [value]
                                    player_high_cards += [value]
                            player_high_cards = sorted(player_high_cards)
                            self._scores[player] = player_high_cards[-1]
                        high_cards = sorted(high_cards)
                        if high_cards[-1] > high_cards[-2]:
                            print(high_cards)
                            winning_score = high_cards[-1]
                            for player in self._scores:
                                if self._scores[player] == winning_score:
                                    player_cards = Hand.get_cards(self._hands[player])[:2]
                                    player_cards[0] = Card.__repr__(player_cards[0])
                                    player_cards[1] = Card.__repr__(player_cards[1])
                                    print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        else:
                            winning_score = high_cards[-1]
                            winning_players = []
                            winning_hands = []
                            player_cards = []
                            for player in self._scores:
                                if self._scores[player] == winning_score:
                                    winning_players += [player]
                                    winning_hands += [self._hands[player]]
                                player_cards1 = Hand.get_cards(self._hands[player])[:2]
                                player_cards1[0] = Card.__repr__(player_cards1[0])
                                player_cards1[1] = Card.__repr__(player_cards1[1])
                                player_cards += player_cards1
                            print(winning_hands)
                            print(', '.join(winning_players) + ' all tied to win with :', ' '.join(player_cards))


    def mult_two_pairs(self):

        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
        each_score = sorted(each_score)
        if each_score[-1] == 3 and each_score[-2] == 3:
            pair_ranks = []
            for player in self._players:
                ranks = Hand.get_ranks(self._hands[player])
                for value in list(set(ranks)):
                    if ranks.count(value) == 2:
                        pair_ranks += [value]
                        self._scores[player] = value
            pair_ranks = sorted(pair_ranks)
            if pair_ranks[-1] > pair_ranks[-2]:
                winning_score = pair_ranks[-1]
                for player in self._scores:
                    if self._scores[player] == winning_score:
                        player_cards = Hand.get_cards(self._hands[player])[:2]
                        player_cards[0] = Card.__repr__(player_cards[0])
                        player_cards[1] = Card.__repr__(player_cards[1])
                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        print(self._hands)
            else:
                high_pair = pair_ranks[-1]     
                pair_ranks = []
                for player in self._players:
                    ranks = Hand.get_ranks(self._hands[player])
                    for value in list(set(ranks)):
                        if ranks.count(value) == 2 and value != high_pair:
                            pair_ranks += [value]
                            self._scores[player] = value
                pair_ranks = sorted(pair_ranks)
                if pair_ranks[-1] > pair_ranks[-2]:
                    winning_score = pair_ranks[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                            print(self._hands)
                else:
                    high_pair2 = pair_ranks[-1]     
                    pair_ranks = []
                    for player in self._players:
                        ranks = Hand.get_ranks(self._hands[player])
                        for value in list(set(ranks)):
                            if value != high_pair and value != high_pair2:
                                pair_ranks += [value]
                                self._scores[player] = value
                    pair_ranks = sorted(pair_ranks)
                    if pair_ranks[-1] > pair_ranks[-2]:
                        winning_score = pair_ranks[-1]
                        for player in self._scores:
                            if self._scores[player] == winning_score:
                                player_cards = Hand.get_cards(self._hands[player])[:2]
                                player_cards[0] = Card.__repr__(player_cards[0])
                                player_cards[1] = Card.__repr__(player_cards[1])
                                print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                                print(self._hands)
                    else:
                        winning_score = pair_ranks[0]
                        winning_players = []
                        winning_hands = []
                        player_cards = []
                        for player in self._scores:
                            winning_players += [player]
                            winning_hands += [self._hands[player]]
                            player_cards1 = Hand.get_cards(self._hands[player])[:2]
                            player_cards1[0] = Card.__repr__(player_cards1[0])
                            player_cards1[1] = Card.__repr__(player_cards1[1])
                            player_cards += player_cards1
                        print(winning_hands)
                        print(', '.join(winning_players) + ' all tied to win with :', ' '.join(player_cards))

    def mult_three_of_a_kinds(self):

        each_score = []
        for player in self._players:
            self._scores[player] = Hand.rank(self._hands[player])
            each_score += [self._scores[player]]
            print(self._hands[player])
        each_score = sorted(each_score)
        if each_score[-1] == 4 and each_score[-2] == 4:
            three_ranks = []
            for player in self._players:
                ranks = Hand.get_ranks(self._hands[player])
                for value in list(set(ranks)):
                    if ranks.count(value) == 3:
                        three_ranks += [value]
                        self._scores[player] = value
            three_ranks = sorted(three_ranks)
            if three_ranks[-1] > three_ranks[-2]:
                winning_score = three_ranks[-1]
                for player in self._scores:
                    if self._scores[player] == winning_score:
                        player_cards = Hand.get_cards(self._hands[player])[:2]
                        player_cards[0] = Card.__repr__(player_cards[0])
                        player_cards[1] = Card.__repr__(player_cards[1])
                        print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                        print(self._hands)
            else:
                three_card = three_ranks[-1]
                three_ranks = []
                for player in self._players:
                    ranks = Hand.get_ranks(self._hands[player])
                    for value in list(set(ranks)):
                        if value != three_card:
                            three_ranks += [value]
                            self._scores[player] = value
                three_ranks = sorted(three_ranks)
                if three_ranks[-1] > three_ranks[-2]:
                    winning_score = three_ranks[-1]
                    for player in self._scores:
                        if self._scores[player] == winning_score:
                            player_cards = Hand.get_cards(self._hands[player])[:2]
                            player_cards[0] = Card.__repr__(player_cards[0])
                            player_cards[1] = Card.__repr__(player_cards[1])
                            print(player, "won. Their hand:", " ".join(player_cards), Hand.type(self._hands[player]))
                            print(self._hands)

                else:
                    winning_score = three_ranks[-2]
                    winning_players = []
                    winning_hands = []
                    player_cards = []
                    for player in self._scores:
                        winning_players += [player]
                        winning_hands += [self._hands[player]]
                        player_cards1 = Hand.get_cards(self._hands[player])[:2]
                        player_cards1[0] = Card.__repr__(player_cards1[0])
                        player_cards1[1] = Card.__repr__(player_cards1[1])
                        player_cards += player_cards1
                    print(winning_hands)
                    print(', '.join(winning_players) + ' all tied to win with :', ' '.join(player_cards))