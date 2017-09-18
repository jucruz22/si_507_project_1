# Do not change import statements.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


class TestClassCard(unittest.TestCase):
    # bug = face card translation?

    def setUp(self):  # similar to the __init__ step in creating a class, so use self.instance
        self.fc = Card(2, 12)  # face card -- queen of Hearts
        self.nc = Card(0, 5)  # number card -- 5 of Diamonds
        self.ac = Card(3, 1)  # Ace card - Ace of spades

    def test_constructor(self):
        # testing that constructor creates an instance of class Card
        self.assertIsInstance(self.fc, Card)

    def test_instance_variable_suit(self):
        self.assertEqual(self.fc.suit, 'Hearts',
                         'card = queen of hearts should have suit Hearts')

    def test_instance_variable_rank_str(self):
        self.assertEqual(self.fc, 'Queen',
                         'card = queen of hears should have rank Queen')

    def test_instance_variable_rank_int(self):
        self.assertEqual(
            self.nc, 5, 'card = 5 of Diamonds should have rank of 5')

    def test_instance_variable_rank_num_1(self):
        self.assertEqual(
            self.fc, 12, 'card = queen of hearts should have rank_num = 12')

    def test_instance_variable_rank_num_2(self):
        self.assertEqual(
            self.nc, 5, 'card = 5 of diamonds should have rank_num = 5')

    def test_str(self):
        self.assertEqual(print(self.nc), '5 of Diamonds',
                         'appropriate string should return')

    def tearDown(self):
        pass


class TestClassDeck(unittest.TestCase):
    def setUp(self):
        self.d = Deck()  # a deck instance
        self.cards = self.d.cards  # d.cards = list of card objects, ordered by suit and rank
        self.first_card = self.cards[0]
        self.last_card = self.cards[51]
        # print (self.d.__str__().split('\n'))
        popped_deck = self.d.pop_card()
        # print (self.d.__str__().split('\n'))
        '''last card (top card) in ordered deck is King of Spades'''

    def test_constructor(self):
        # confirming that d is an instance of class Deck
        self.assertIsInstance(self.d, Deck)

    def test_instance_variable_list(self):
        # .cards instance variable is a list object
        self.assertEqual(type(self.cards), list,
                         'instance of Deck should be a list')

    def test_instance_variable_length(self):
        # cards list is 52 items long
        self.assertEqual(len(self.cards), 52,
                         'length of cards list should = 52')

    def test_deck_str(self):
        # string returned is 52 lines
        # split deck string name by its newlines
        string_list = self.d.__str__().split('\n')
        self.assertEqual(len(
            string_list), 52, 'string method should return multi-lines, one for each card')

    def test_pop_card(self):
        # test that deck is empty when pop all cards
        d = Deck()  # create a deck instance
        for i in range(52):  # i reflects index values of deck, so the range should only go to 52
            d.pop_card()  # pop all 52 cards off
        self.assertTrue(
            len(d.cards) == 0, 'after 52 pops all cards should be removed from d.cards list')

    def test_shuffle(self):
        # confirm that order of cards list changes after shuffle method invoked
        d = Deck()
        dd = Deck()
        d.shuffle()
        self.assertFalse(
            d.cards == dd.cards, "shuffle ensures the order of these two decks are different")

    def test_replace_cards(self):
        # confirm that missing card is replaced
        d = Deck()
        cards = d.cards  # make a list of card instances in that deck
        # index a single card that we want replaced later
        to_be_replaced = cards[0]
        cards.pop(0)  # now pop that card out of the list
        d.replace_card(to_be_replaced)  # invoke the replace_card method
        self.assertTrue(to_be_replaced in d.cards,
                        'correct card has been re-inserted into deck')

    def test_deal_hand(self):
        # test that correct hand size is returned
        d = Deck()  # deck instance with d.cards = list of card instances
        d.shuffle()  # shuffle the cards well
        # print (d)
        hand = d.deal_hand(4)
        # creates a list of strings for each card so you can see what's delt
        hand_cards = [str(c) for c in hand]
        # print (hand_cards)
        self.assertTrue(len(hand == 4))

    def test_deal_hand_full(self):
        # testing that full hand means all cards are removed from deck and transfered into hand
        d=Deck()
        cards=d.cards
        d.shuffle()
        hand=d.deal_hand(52)  # returns list of card objects of that hand size
        # converts that list of card objects into actual strings that represent the type of card
        hand_cards=[str(c) for c in hand]
        self.assertTrue(len(hand) == 52, 'hand contains all cards')
        self.assertTrue(len(cards) == 0,
                        'tesing all cards are removed from deck')

    def test_sort_cards(self):
        # testing that default cards list order is resumed after sort
        d1=Deck()
        d2=Deck()
        d2.shuffle()
        d2.sort_cards()
        self.assertTrue(d1.cards == d2.cards,
                        'sorting reverts cards list to original state before shuffling')

    def tearDown(self):
        # used to close stuff, close a file, a database, etc.
        # use specific methods to delete a file, depending on what type it is
        pass  # for now

class TestWar(unittest.TestCase):
    def test_war_type(self):
        # testing that a tuple is returned from the war function
        w=play_war_game(testing=True)  # initializing war game function
        self.assertEqual(type(w), tuple,'function should return a tuple')

    def test_war_first_tuple(self):
        # tesing that
        w=play_war_game(testing=True)
        options=['Player1', 'Player2', 'Tie']
        self.assertTrue(w[0] in options,'first item in tuple should name the winner or a tie')

    def test_war_two_integers(self):
        w=play_war_game(testing=True)
        self.assertEqual(type(w[1]), int,'second item in tuple should be a points integer')
        self.assertEqual(type(w[2]), int,'third item in tuple should be a points integer')

    def test_war_winners(self):
        w=play_war_game(testing=True)
        if w[0] == 'Player1':  # if player one wins...
            self.assertTrue(w[1] > w[2], 'player one should have more points than player two')  # then points of player 1 > points of player two
        elif w[0] == 'Player2':
            self.assertTrue(w[2] > w[1],'player two should have more points than player one')  # and vice versa
        else:
            self.assertTrue(w[1] == w[2],'player one and two should have same number of points')


class TestShowSong(unittest.TestCase):
    # test that show_song returns a single instance of class Song
    def test_song_instance(self):
        s=show_song()  # default parameter = "winner"
        self.assertIsInstance(s, Song, 'testing instance')

    # test that when calling string method on song instance, "SearchTerm" is in the name
    def test_song_search_term(self):
        s=show_song("Beauty")
        self.assertTrue("Beauty" in s.__str__())


if __name__ == '__main__':
    # makes sure that only runs test cases when called from command line, and not when running a separate file that imports THIS test case file
    unittest.main(verbosity=2)
