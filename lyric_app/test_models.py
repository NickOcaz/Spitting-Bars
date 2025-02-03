from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Lyric, Genre

class LyricModelTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a genre
        self.genre = Genre.objects.create(name='Test Genre', excerpt='Test Excerpt')
        # Create a lyric
        self.lyric = Lyric.objects.create(
            title='Test Lyric',
            artist=self.user,
            lyric='Test Lyric Content',
            genre=self.genre,
            status=0,
        #    is_protected=False,
            is_approved=False
        )

    def test_lyric_creation(self):
        # Test lyric creation
        self.assertTrue(isinstance(self.lyric, Lyric))
        self.assertEqual(self.lyric.__str__(), self.lyric.title)
        self.assertEqual(self.lyric.artist, self.user)
        self.assertEqual(self.lyric.lyric, 'Test Lyric Content')
        self.assertEqual(self.lyric.genre, self.genre)
        self.assertEqual(self.lyric.status, 0)
      #  self.assertEqual(self.lyric.is_protected, False)
        self.assertEqual(self.lyric.is_approved, False)
        

    def test_lyric_str(self):
        # Test the __str__ method of the Lyric model
        self.assertEqual(self.lyric.__str__(), self.lyric.title)

    def test_lyric_status(self):
        # Test the status field of the Lyric model
        self.assertEqual(self.lyric.status, 0)

   # def test_lyric_is_protected(self):
   #     # Test the is_protected field of the Lyric model
   #     self.assertEqual(self.lyric.is_protected, False)

    def test_lyric_is_approved(self):
        # Test the is_approved field of the Lyric model
        self.assertEqual(self.lyric.is_approved, False)

    def test_lyric_timestamps(self):
        # Test the created_at and updated_at fields of the Lyric model
        self.assertTrue(self.lyric.created_at)
        
    def test_lyric_update(self):
        # Test updating a lyric
        self.lyric.title = 'Updated Test Lyric'
        self.lyric.save()
        self.assertEqual(self.lyric.title, 'Updated Test Lyric')
    # generate a unit test that checks for an error when a user tries to create a lyric without a title
    def test_lyric_no_title(self):
        with self.assertRaises(ValidationError):
            lyric = Lyric(
                title='',
                artist=self.user,
                lyric='Test Lyric Content',
                genre=self.genre,
                status=0,
            #    is_protected=False,
                is_approved=False
            )
            lyric.save()
    # generate a unit test that checks for an error when a user tries to create a title with a title that is too long
    def test_lyric_title_too_long(self):
        with self.assertRaises(ValidationError):
            lyric = Lyric(
                title='x' * 256,
                artist=self.user,
                lyric='Test Lyric Content',
                genre=self.genre,
                status=0,
               # is_protected=False,
                is_approved=False
            )
            lyric.save()
    # generate a unit test that checks for an error when a user tries to create a lyric without a lyric content
    def test_lyric_no_lyric(self):
        with self.assertRaises(ValidationError):
            lyric = Lyric(
                title='Test Lyric',
                artist=self.user,
                lyric='',
                genre=self.genre,
                status=0,
             #   is_protected=False,
                is_approved=False
            )
            lyric.save()