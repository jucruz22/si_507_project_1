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
    def setUp(self):
        pass

    def tearDown(self):
        pass
class TestClassDeck(unittest.TestCase):
    def setUp(self):
        # put any common instances in this function
        # i.e. creating a card, opening a file, creating an instances
        pass # for now

    def test_constructor(self):
        pass

    def test_shuffle(self):
        pass

    def tearDown(self):
        # used to close stuff, close a file, a database, etc.
        # use specific methods to delete a file, depending on what type it is
        pass #for now
