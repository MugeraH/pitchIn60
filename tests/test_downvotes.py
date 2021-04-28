import unittest
from app.models import Pitch, Downvote,User


class DownvoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Mugera = User(username='wiko', password='banana', email='wiko@ms.com')  
        self.new_pitch = Pitch(title='Humour',pitch="He who laughs last is the one who got the joke the last",category="Humour",user = self.user_Mugera)
        self.new_downvote = Downvote(downvote_count=8,pitch=self.new_pitch,user=self.user_Mugera) 
        
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Downvote.query.delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_downvote, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_downvote.downvote_count, 8)
        self.assertEquals(self.new_downvote.user, self.user_Mugera)
        self.assertEquals(self.new_downvote.pitch, self.new_pitch)

    def test_save_downupvote(self):
        self.new_downvote.add_downvote()
        self.assertTrue(len(Downvote.query.all()) > 0)
        
    

       