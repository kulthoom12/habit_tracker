from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Habit


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.habit = Habit.objects.create(
            user=self.user,
            title='Read',
            frequency='daily'
        )

    def test_habit_creation(self):
        habit = Habit.objects.get(title='Read')
        self.assertEqual(habit.user.username, 'testuser')
        self.assertEqual(habit.frequency, 'daily')
        self.assertEqual(habit.streak, 0)
        self.assertFalse(habit.completed_today)

    def test_update_streak_completed(self):
        self.habit.completed_today = True
        self.habit.update_streak()
        self.assertEqual(self.habit.streak, 1)

    def test_update_streak_not_completed(self):
        self.habit.completed_today = False
        self.habit.streak = 3
        self.habit.update_streak()
        self.assertEqual(self.habit.streak, 0)


class HabitViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.habit = Habit.objects.create(
            user=self.user,
            title='Read',
            frequency='daily'
        )

    def test_home_page_requires_login(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/login/?next=/')

    def test_login_and_access_home(self):
        self.assertTrue(self.client.login(
            username='testuser', password='12345'))
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'habits/index.html')

    def test_add_habit_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('habits_create'), {
            'title': 'Exercise',
            'description': 'Daily exercise',
            'frequency': 'daily',
            'completed_today': True
        })

        self.assertEqual(Habit.objects.filter(title='Exercise').count(), 1)
        self.assertRedirects(response, reverse('home'))

    def test_edit_habit_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('habits_update', args=[self.habit.id]),
            {
                'title': 'Read Updated',
                'description': 'Read books daily',
                'frequency': 'daily',
                'completed_today': True
            }
        )

        self.habit.refresh_from_db()
        self.assertEqual(self.habit.title, 'Read Updated')
        self.assertTrue(self.habit.completed_today)
        self.assertRedirects(response, reverse('home'))
