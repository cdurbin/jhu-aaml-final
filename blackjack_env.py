import random
import copy

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

        self.cards = cards
        self.deal_seq = []
        self.number_of_decks = number_of_decks
        self.total_cards = 52 * self.number_of_decks
        self.initial_deck_state = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 'deck_percent': 0.0}
        self.state = copy.deepcopy(self.initial_deck_state)

    def maybe_shuffle_cards(self):
        total_cards = 52 * self.number_of_decks
        if len(self.deal_seq) < 0.1 * total_cards:
            # print('SHUFFLING...')
            combined_decks = self.cards * self.number_of_decks
            random.shuffle(combined_decks)
            self.deal_seq = combined_decks
            self.state = copy.deepcopy(self.initial_deck_state)

    def deal_card(self):
        if len(self.deal_seq) == 0:
            self.maybe_shuffle_cards()
        next_card = self.deal_seq.pop(0)
        # Note we can't see one of the dealer's cards until the end, but since this is
        # called after we've placed our bet and the state won't be used until next hand
        # it is fine to update the state while dealing
        self.state[next_card['value']] += 1

        deck_percent = (self.total_cards - len(self.deal_seq)) / self.total_cards
        self.state['deck_percent'] = deck_percent
        return next_card


class Blackjack:
    def __init__(self):
        number_of_decks = 1
        self.deck = CardDeck(number_of_decks)
        self.agent_total = 0
        self.usable_ace = 0
        self.dealer_visible_total = 0
        self.dealer_total = 0
        self.dealer_ace = 0
        self.current_state = None

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
        if self.agent_total > 21:
            new_state = 201
        else:
            new_state = self.construct_state()
        return new_state

    def get_deck_state(self):
        return self.deck.state

    def reset(self):
        self.deck.maybe_shuffle_cards()
        self.agent_total = 0
        self.usable_ace = False
        self.dealer_visible_total = 0
        self.dealer_total = 0
        self.dealer_ace = False
        self.current_state = None

        return self.get_deck_state()

    def deal_hand(self):
        # deal a face up card and a second card to the dealer
        dealer_face_up_card = self.deck.deal_card()
        dealer_face_down_card = self.deck.deal_card()
        self.dealer_total = dealer_face_up_card['value'] + dealer_face_down_card['value']
        self.dealer_visible_total = dealer_face_up_card['value']
        if dealer_face_up_card['value'] == 1 or dealer_face_down_card['value'] == 1:
            self.dealer_ace = True
            self.dealer_total += 10

        # deal two cards to the agent
        card_1 = self.deck.deal_card()
        card_2 = self.deck.deal_card()
        self.agent_total = card_1['value'] + card_2['value']
        if card_1['value'] == 1 or card_2['value'] == 1:
            self.usable_ace = True
            self.agent_total += 10

        # check to see if the agent has a natural (ace + face card)
        if self.agent_total == 21:
            if self.dealer_total == 21:
                self.current_state = 202    # tie game
            else:
                self.current_state = 303    # agent natural 1.5x win

        # otherwise, deal enough cards to the agent so that the total is >11
        else:
            while self.agent_total < 12:
                new_card = self.deck.deal_card()
                self.agent_total += new_card['value']
                if new_card['value'] == 1 and self.usable_ace == False and self.agent_total < 12:
                    self.usable_ace = True
                    self.agent_total += 10
            self.current_state = self.construct_state()

        return self.current_state

    def execute_action(self, action):
        # action is 'stay'
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
            if new_state == 201:
                reward = -1
                game_end = True
            else:
                reward = 0
                game_end = False

        self.current_state = new_state
        return new_state, reward, game_end


