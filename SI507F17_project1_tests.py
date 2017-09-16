## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class TestClassCard(unittest.TestCase):
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
        self.cards = self.d.cards # d.cards = list of card objects

    def test_constructor(self):
        # confirming that d is an instance of class Deck
        self.assertIsInstance(self.d,Deck)

    def test_instance_variable_list(self):
        # .cards instance variable is a list object
        self.assertEqual(type(self.cards),list,'instance of Deck should be a list')

    def test_instance_variable_length(self):
        # cards list is 52 items long
        self.assertEqual(len(self.cards),52,'length of cards list should = 52')

    def test_str(self):
        pass # how to write this concisely?
        '''* The Deck string method should return a multi-line string with one line for each printed representation of a card in the deck. So a complete deck should have a 52-line string of strings like "Ace of Diamonds", "Two of Diamonds", etc.'''

    def test_pop_card_len(self):
        # testing that cards list is one less when use the pop_card method
        self.d.pop_card()
        self.assertEqual(len(self.cards),51,'length of cards list decrease by 1 when pop card')

    def test_pop_card_last(self):
        # testing that LAST card is removed = i.e. King of Spades
        self.d.pop_card(1)
        self.assertTrue("King of Spades" not in self.d.__str__(),'cards should be removed from top to bottom')

    def test_pop_card_empty(self):
        # testing that cards list is empty if you use pop_card method 52 times
        self.d.pop_card(51)
        self.assertEqual(len(self.d.cards),0,'deck is empty once you pop 52 times')

    def test_shuffle(self):
        	# use string method here
    		# create a list of 52 name strings for each card
    				cards_strings = [str(c) for c in self.cards]
    				cards_strings_shuffle =
    			# check lists are/aren't equal before shuffling or after shuffling
    			# also check that the length of these lists is the same (i.e. started/ended with 52 cards)
    		# a = [1,2,3]
    		# b = [3,2,1]
    		# a == b, if True, then didn't shuffle -- if False, then did shuffle
    		# len(a) == len(b)
            
    '''* Deck has a method shuffle which accepts no external input and shuffles the self.cards list in the Deck at that time so that it has a random order.'''

    def tearDown(self):
        # used to close stuff, close a file, a database, etc.
        # use specific methods to delete a file, depending on what type it is
        pass #for now

'''
* A class Deck


	* Deck has a method replace_card which accepts a Card instance as input. If the card instance input into the method is NOT already in the deck, it is added back to the deck. If it IS already in the deck, nothing changes about the Deck (a deck should not have any duplicate cards as a result of calling this method).

	* Deck has a method sort_cards which should organize the cards remaining in the deck into an order such that they are in ascending order by suit: Diamonds, then Clubs, then Hearts, then Spades.

	* Deck has a method deal_hand which takes a required input hand_size, an integer representing the number of cars in the hand. It should return a list of Card objects that make up the hand dealt. A hand should be able to be dealt up to the full size of the current deck (e.g. if 3 cards have been removed from the deck and not replaced, it should be impossible to deal a 52-card hand, but if no cards have been removed, it should be possible)


* A function play_war_game

	* The function has one keyword parameter *testing*, whose default value is False. When the function is called with testing=True, the function does not make any print statements, making it easier to see tests.
		* (NOTE: You do not have to test this -- it is difficult to test print statements, because print is for people! However, when testing this function, you should ALWAYS invoke it with testing=True and NEVER with the default value, or the tests will be very difficult ot read.)

	* The play_war_game function should initialize two Deck instances, representing Player 1 and Player 2, inside its function scope and simulate a variation on the card game of War (http://www.bicyclecards.com/how-to-play/war/). This happens with no external input. There are 3 possible outcomes: the Player1 score is larger than the Player2 score and Player1 wins, the Player2 score is larger than the Player1 score and Player2 wins, or the two scores are the same and there is a tie.

	* The play_war_game function should always return a tuple of a string and two integers, where the string is either "Player1", "Player2", or "Tie", and the integers represent the Player1 score and the Player2 score, respectively.

* A function show_song

	* The show_song function takes a string as input to use as a search term for songs on iTunes. Its default value is "Winner", but you should be able to search for any search term with this function.

	* The show_song function invokes a function from the helper_functions file (which you do NOT have to test!), that gets data from the iTunes Search API based on this search term. It creates a list of Song objects, using the Song class definition from the helper_functions file.

	* The show_song function should return a single instance of class Song (whose definition you can see in helper_functions.py, but which you do NOT have to test).
		- s = show_song()
		- self.assertIsInstance(s,Song)
		- self.assertTrue(isinstance(s,Song)

		- s2 = show_song('Bowie')
		- print(s2)
		- self.assertTrue('Bowie' in str(str2))
'''

if __name__ == '__main__':
    #makes sure that only runs test cases when called from command line, and not when running a separate file that imports THIS test case file
    unittest.main(verbosity=2)
