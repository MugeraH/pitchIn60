import unittest
from app.models import Pitch,Upvote,User


class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Mugera = User(username='wiko', password='banana', email='wiko@ms.com')  
        self.new_pitch = Pitch(title='Humour',pitch="He who laughs last is the one who got the joke the last",category="Humour",user = self.user_Mugera)
        self.new_upvote = Upvote(upvote_count=8,pitch=self.new_pitch,user=self.user_Mugera) 
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Upvote.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_upvote, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_upvote.upvote_count, 8)
        self.assertEquals(self.new_upvote.user, self.user_Mugera)
        self.assertEquals(self.new_upvote.pitch, self.new_pitch)

    def test_save_downupvote(self):
        self.new_upvote.add_upvote()
        self.assertTrue(len(Upvote.query.all()) > 0)
        
    

       