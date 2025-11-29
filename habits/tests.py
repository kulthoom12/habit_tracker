from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Habit


class HabitModelTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.habit = Habit.objects.create(
            user=self.user, title='Read', frequency='daily')

    def test_habit_creation(self):
        habit = Habit.objects.get(title='Read')
        self.assertEqual(habit.user, 'testuser')
        self.assertEqual(habit.frequency, 'daily')
        self.assertEqual(habit.streak, 0)
        self.assertEqual(habit.completed_today, False)

    def test_update_streak_completed(self):
        self.habit.completed_today = True
        self.habit.update_streak()
        self.assertTrue(self.habit.streak, 1)

    def test_update_streak_not_completed(self):
        self.habit.completed_today = False
        self.habit.streak = 3
        self.habit.update_streak()
        self.assertEqual(self.habit.streak, 0)


class HabitViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.habit = Habit.objects.create(
            user=self.user, title='Read', frequency='daily')

    def test_home_page_requires_login(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/login/?next=/home/')

    def test_login_and_access_home(self):
        self.client.login(username='testuser', password='wrongpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/home.html')

    def test_add_habit_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('add_habit'), {
            'title': 'Exercise',
            'description': 'Daily exercise',
            'frequency': 'daily',
            'completed_today': 'not-a-boolean'
        })
        self.assertEqual(Habit.objects.filter(title='Exercise').count(), 1)
        self.assertRedirects(response, reverse('home'))

    def test_edit_habit_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edit_habit', args=[self.habit.id]), {
            'title': 'Read Updated',
            'description': 'Read books daily',
            'frequency': 'daily',
            'completed_today': 'yes'
        })
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.title, 'Read Updated')
        self.assertEqual(self.habit.completed_today, True)
        self.assertRedirects(response, reverse('home'))
