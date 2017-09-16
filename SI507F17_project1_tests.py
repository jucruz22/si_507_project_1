## Do not change import statements.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class TestClassCard(unittest.TestCase):
    # bug = face card translation?

    def setUp(self): # similar to the __init__ step in creating a class, so use self.instance
        self.fc = Card(2,12) # face card -- queen of Hearts
        self.nc = Card(0,5) # number card -- 5 of Diamonds
        self.ac = Card(3,1) # Ace card - Ace of spades

    def test_constructor(self):
        self.assertIsInstance(self.fc,Card) # testing that constructor creates an instance of class Card

    def test_instance_variable_suit(self):
        self.assertEqual(self.fc.suit,'Hearts','card = queen of hearts should have suit Hearts')

    def test_instance_variable_rank_str(self):
        self.assertEqual(self.fc,'Queen','card = queen of hears should have rank Queen')

    def test_instance_variable_rank_int(self):
        self.assertEqual(self.nc,5,'card = 5 of Diamonds should have rank of 5')

    def test_instance_variable_rank_num_1(self):
        self.assertEqual(self.fc,12,'card = queen of hearts should have rank_num = 12')

    def test_instance_variable_rank_num_2(self):
        self.assertEqual(self.nc,5,'card = 5 of diamonds should have rank_num = 5')

    def test_str(self):
        self.assertEqual(print(self.nc),'5 of Diamonds','appropriate string should return')

    def tearDown(self):
        pass

class TestClassDeck(unittest.TestCase):
    def setUp(self):
        self.d = Deck() # a deck instance
        self.cards = self.d.cards # d.cards = list of card objects, ordered by suit and rank
        self.first_card = self.cards[0]
        self.last_card = self.cards[51]
        # print (self.d.__str__().split('\n'))
        popped_deck = self.d.pop_card()
        # print (self.d.__str__().split('\n'))
        '''last card (top card) in ordered deck is King of Spades'''

    def test_constructor(self):
        # confirming that d is an instance of class Deck
        self.assertIsInstance(self.d,Deck)

    def test_instance_variable_list(self):
        # .cards instance variable is a list object
        self.assertEqual(type(self.cards),list,'instance of Deck should be a list')

    def test_instance_variable_length(self):
        # cards list is 52 items long
        self.assertEqual(len(self.cards),52,'length of cards list should = 52')

    def test_deck_str(self):
        string_list = self.d.__str__().split('\n')
        self.assertEqual(len(string_list),52,'string method should return multi-lines, one for each card')

    def test_pop_card(self):
        d = Deck()
        for i in range(52):
            d.pop_card()
        self.assertTrue(len(d.cards)==0,'test')

    def test_shuffle(self):
        # confirm that order of cards changes after shuffle method invoked
        d = Deck()
        dd = Deck()
        d.shuffle()
        self.assertFalse(d==dd,"shuffle ensures the order of these two decks are different")

    def test_deal_hand(self):
        # test that correct hand size is returned
        d = Deck() #deck instance with d.cards = list of card instances
        #shuffle the deck well
        d.shuffle()
        # print (d)
        hand = d.deal_hand(4)
        hand_cards = [str(c) for c in hand] # creates a list of strings for each card so you can see what's delt
        # print (hand_cards)
        self.assertTrue(len(hand_cards)==4)

    def test_deal_hand_full(self):
        d = Deck()
        d.shuffle()
        hand = d.deal_hand(52) #returns list of card objects of that hand size
        hand_cards = [str(c) for c in hand] #converts that list of card objects into actual strings that represent the type of card
        self.assertTrue(len(d.cards) == 0, 'tesing all cards are removed from deck')

    def test_sort_cards(self):
        d = Deck()
        dd = Deck()
        dd.shuffle()
        dd.sort_cards()
        self.assertTrue(d.__str__()==dd.__str__(),'sorting reverts cards list to original state before shuffling')
        # when cards list is freshly made, it's already sorted right?
        # so we'd have to use shuffle, then sort again, to determine that sort returns self.cards list order to its original state

    def tearDown(self):
        # used to close stuff, close a file, a database, etc.
        # use specific methods to delete a file, depending on what type it is
        pass #for now

class TestWar(unittest.TestCase):
    def test_war_type(self):
        war = play_war_game(testing=True)
        self.assertEqual(type(war), tuple)

    def test_war_first_position_of_tuple(self):
        war = play_war_game(testing=True)
        self.assertTrue(war[0] in ['Player1', 'Player2', 'Tie'])

    def test_war_two_integers(self):
        war = play_war_game(testing=True)
        self.assertEqual(type(war[1]), int)
        self.assertEqual(type(war[2]), int)

    def test_war_winners(self):
        war = play_war_game(testing=True)
        if war[0] == 'Player1':
            self.assertTrue(war[1]>war[2])
        elif war[0] == 'Player2':
            self.assertTrue(war[2]>war[1])
        else:
            self.assertTrue(war[1]==war[2])


class TestShowSong(unittest.TestCase):
    # test that show_song returns a single instance of class Song
    def test_song_instance(self):
        s = show_song() # default parameter = "winner"
        self.assertIsInstance(s,Song,'testing instance')

    # test that when calling string method on song instance, "SearchTerm" is in the name
    def test_song_search_term(self):
        s = show_song("Beauty")
        self.assertTrue("Beauty" in s.__str__())


if __name__ == '__main__':
    #makes sure that only runs test cases when called from command line, and not when running a separate file that imports THIS test case file
    unittest.main(verbosity=2)
