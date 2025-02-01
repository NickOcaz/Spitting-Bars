from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Lyric, Genre

class LyricAppViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.genre = Genre.objects.create(name='Test Genre', excerpt='Test Excerpt')
        self.lyric = Lyric.objects.create(
            title='Test Lyric',
            artist=self.user,
            lyric='Test Lyric Content',
            genre=self.genre,
            status=0,
            is_protected=False,
            is_approved=False
        )

    # no genre list view 
    # def test_genre_list_view(self):
    #     # Test the genre list view
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.get(reverse('genre_list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'lyric_app/genre_list.html')
        

    def test_lyric_list_view(self):
        # Test the lyric list view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lyric_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lyric_app/lyric_list.html')
        

    def test_lyric_detail_view(self):
        # Test the lyric detail view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lyric_detail', args=[self.lyric.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lyric_app/lyric_detail.html')
        

    def test_lyric_create_view(self):
        # Test the lyric create view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lyric_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lyric_app/lyric_create.html')

    def test_lyric_edit_view(self):
        # Test the lyric edit view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lyric_edit', args=[self.lyric.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lyric_app/lyric_edit.html')
        

    def test_lyric_delete_view(self):
        # Test the lyric delete view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('lyric_delete', args=[self.lyric.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_page'))
        

    def test_user_page_view(self):
        # Test the user page view
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('user_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_page.html')