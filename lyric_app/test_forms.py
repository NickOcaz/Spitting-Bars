from django.test import TestCase
from .forms import LyricForm
from .models import Genre, Lyric
from django.contrib.auth.models import User

class LyricFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.genre = Genre.objects.create(name='Test Genre', excerpt='Test Excerpt')

    def test_lyric_form_valid(self):
        # Test the form with valid data
        form = LyricForm(data={
            'title': 'Test Lyric',
            'lyric': 'Test Lyric Content',
            'genre': self.genre.pk,
            'status': 0,
            'is_protected': False
        })
        self.assertTrue(form.is_valid())

    def test_lyric_form_invalid(self):
        # Test the form with invalid data
        form = LyricForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  # Adjust the expected number of errors

    def test_lyric_form_missing_title(self):
        # Test the form with missing title
        form = LyricForm(data={
            'title': '',
            'lyric': 'Test Lyric Content',
            'genre': self.genre.pk,
            'status': 0,
            'is_protected': False
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_lyric_form_missing_lyric(self):
        # Test the form with missing lyric content
        form = LyricForm(data={
            'title': 'Test Lyric',
            'lyric': '',
            'genre': self.genre.pk,
            'status': 0,
            'is_protected': False
        })
        self.assertFalse(form.is_valid())
        self.assertIn('lyric', form.errors)

    def test_lyric_form_missing_genre(self):
        # Test the form with missing genre
        form = LyricForm(data={
            'title': 'Test Lyric',
            'lyric': 'Test Lyric Content',
            'genre': '',
            'status': 0,
            'is_protected': False
        })
        self.assertFalse(form.is_valid())
        self.assertIn('genre', form.errors)

    def test_lyric_form_invalid_status(self):
        # Test the form with invalid status
        form = LyricForm(data={
            'title': 'Test Lyric',
            'lyric': 'Test Lyric Content',
            'genre': self.genre.pk,
            'status': 'invalid',
            'is_protected': False
        })
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)

    def test_lyric_form_is_protected(self):
        # Test the form with is_protected field
        form = LyricForm(data={
            'title': 'Test Lyric',
            'lyric': 'Test Lyric Content',
            'genre': self.genre.pk,
            'status': 0,
            'is_protected': True
        })
        self.assertTrue(form.is_valid())