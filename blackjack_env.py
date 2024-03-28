import random

SUITS = ['club', 'spade', 'heart', 'diamond']

class CardDeck:
    def __init__(self, number_of_decks=1):
        cards = []
        for i in range(2, 11): # Cards 2 through 10
            for suit in SUITS:
                card = { 'name': i, 'value': i, 'suit': suit }
                cards.append(card)

        # Add the aces
        for suit in SUITS:
            card = { 'name': 'ace', 'value': 1, 'suit': suit, 'alt_value': 11 }
            cards.append(card)

        # Add the other face cards
        for face_card in ['jack', 'queen', 'king']:
            for suit in SUITS:
                card = { 'name': face_card, 'value': 10, 'suit': suit }
                cards.append(card)

        # self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
        #               6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        #               10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.cards = cards
        self.deal_seq = []
        self.number_of_decks = number_of_decks

    def shuffle_cards(self):
        self.deal_seq = random.sample(self.cards, 52 * self.number_of_decks)

    def deal_card(self):
        return self.deal_seq.pop(0)

class Blackjack:
    def __init__(self):

        self.deck = CardDeck()
        self.agent_total = 0
        self.usable_ace = 0
        self.dealer_visible_total = 0
        self.dealer_total = 0
        self.dealer_ace = 0
        self.current_state = None
        # self.num_states = 203
        # self.num_actions = 2

    # def get_number_of_states(self):
    #     return self.num_states

    # def get_number_of_actions(self):
    #     return self.num_actions

    def get_state(self):
        return self.current_state

    def construct_state(self):
        state = {
            'agent_total': self.agent_total,
            'usable_ace': self.usable_ace,
            'dealer_visible_total': self.dealer_visible_total,
            'dealer_ace': self.dealer_ace
        }
        return state

    def get_next_state(self):
        new_card = self.deck.deal_card()
        self.agent_total += new_card['value']
        if self.agent_total > 21 and self.usable_ace == True:
            self.usable_ace = False
            self.agent_total -= 10
        # print("Agent drew a", new_card, "and now has", self.agent_total, "points.")
        if self.agent_total > 21:
            new_state = 201
            # new_state = None      # 201 is the losing state
        else:
            new_state = self.construct_state()
        return new_state

    def reset(self):
        self.deck.shuffle_cards()
        self.agent_total = 0
        self.usable_ace = False
        self.dealer_visible_total = 0
        self.dealer_total = 0
        self.dealer_ace = False
        self.current_state = None

        # deal a face up card and a second card to the dealer
        dealer_face_up_card = self.deck.deal_card()
        dealer_face_down_card = self.deck.deal_card()
        self.dealer_total = dealer_face_up_card['value'] + dealer_face_down_card['value']
        self.dealer_visible_total = dealer_face_up_card['value']
        if dealer_face_up_card['value'] == 1 or dealer_face_down_card['value'] == 1:
            self.dealer_ace = True
            self.dealer_total += 10
        # print("Dealer has", self.dealer_card, "and", dealer_face_down_card)
        # print("Dealer has", self.dealer_total, "points.")

        # deal two cards to the agent
        card_1 = self.deck.deal_card()
        card_2 = self.deck.deal_card()
        self.agent_total = card_1['value'] + card_2['value']
        if card_1['value'] == 1 or card_2['value'] == 1:
            self.usable_ace = True
            self.agent_total += 10
        # print("Agent has", card_1, "and", card_2)
        # print("Agent has", self.agent_total, "points.")

        # check to see if the agent has a natural (ace + face card)
        if self.agent_total == 21:
            # TBD - figure out what to do here since it will be important for bet size
            # But for now just shuffle again
            # self.reset()
            if self.dealer_total == 21:
                self.current_state = 202    # tie game
            else:
                self.current_state = 203    # agent wins

        # otherwise, deal enough cards to the agent so that the total is >11
        else:
            while self.agent_total < 12:
                new_card = self.deck.deal_card()
                self.agent_total += new_card['value']
                if new_card['value'] == 1 and self.usable_ace == False and self.agent_total < 12:
                    self.usable_ace = True
                    self.agent_total += 10
                # print("Agent drew a", new_card, "and now has", self.agent_total, "points.")
            # now determine the initial state
            self.current_state = self.construct_state()

        # reset complete; return the initial state
        return self.current_state

    # Use the agent's action to determine the next state and reward
    def execute_action(self, action):
        # action is 'stick'
        if action == 0:
            # dealer's turn
            while self.dealer_total < 17:
                new_card = self.deck.deal_card()
                self.dealer_total += new_card['value']
                if new_card['value'] == 1 and self.dealer_ace == 0 and self.dealer_total < 12:
                    self.dealer_ace = 1
                    self.agent_total += 10
                if self.dealer_total > 21 and self.dealer_ace == 1:
                    self.dealer_ace = 0
                    self.agent_total -= 10
            new_state = None
            if self.dealer_total > 21:
                # dealer busted; agent wins
                new_state = 203
                reward = 1
                game_end = True
            else:
                if self.dealer_total > self.agent_total:
                    # dealer wins
                    new_state = 201
                    reward = -1
                    game_end = True
                elif self.dealer_total < self.agent_total:
                    # agent wins
                    new_state = 203
                    reward = 1
                    game_end = True
                else:
                    # tie
                    new_state = 202
                    reward = 0
                    game_end = True

        # action is 'hit'
        elif action == 1:
            new_state = self.get_next_state()
            # if new_state == None:
            if new_state == 201:
                reward = -1
                game_end = True
            else:
                reward = 0
                game_end = False

        # print("new_state =", new_state, "reward = ", reward, "game_end =", game_end)
        self.current_state = new_state
        return new_state, reward, game_end


