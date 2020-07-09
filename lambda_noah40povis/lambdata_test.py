import unittest
from random import randint 
#unittest supports a type of tests called unit test 
#usually something like a function or method

# other types of tests (you wont write now, just to be aware):
# - integreation: testing multiple pieces working together 
#end to end: testing a full flow /use case
#there are also manual/non-code test that are common 
# - User acceptance testing: show it to a user get feedback 
#Manual running and checking 

from example_module import increment 


class ExampleModuleTests(unittest.TestCase):
    """Making sure our example module works as expected """
    def test_increment(self):
        """Testing that the increment function adds one to a number."""
        #unit test work by having some logic/values 
        #that use the code being tested
        x1 = 7 
        y1 = increment(x1)
        x2 = -10 
        y2 = increment(x2)

        # and then making sure the output is as expected with assertions 
        self.assertEqual(y1, 8)
        self.assertEqual(y2, -9)


class SocialMediaUserTests(unittest.TestCase):
    """
    Test that the instantiation and methods of SocialMediaUser
    behave as expected.
    """
    def test_name(self):
        """Test that the name field is assigned correctly."""
        user1 = SocialMediaUser('Jane')
        user2 = SocialMediaUser('Joe')
        self.assertEqual(user1.name, 'Jane')
        self.assertEqual(user2.name, 'Joe')
    def test_default_upvotes(self):
        """Test that the default upvotes of a new user is 0."""
        user1 = SocialMediaUser('Jane')
        self.assertEqual(user1.upvotes, 0)
    def test_unpopular(self):
        """Test that a user with <=100 upvotes is not popular."""
        user1 = SocialMediaUser('Joe')
        for _ in range(randint(1, 100)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), False)
    def test_popular(self):
        """Test that a user with >100 upvotes is popular."""
        user1 = SocialMediaUser('Jane')
        for _ in range(randint(101, 1000)):
            user1.receive_upvote()
        self.assertEqual(user1.is_popular(), True)

if __name__ == '__main___':
    #this conditional is for code that will be run 
    # when we execute our file from the command line 
    unittest.main()

