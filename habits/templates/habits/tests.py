from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Habit


class HabitModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        # Create a habit for the user
        self.habit = Habit.objects.create(
            user=self.user, title='Read', frequency='daily')

    def test_habit_creation(self):
        habit = Habit.objects.get(title='Read')
        # Error: should be habit.user.username instead of habit.user
        self.assertEqual(habit.user, 'testuser')
        self.assertEqual(habit.frequency, 'daily')
        self.assertEqual(habit.streak, 0)
        # Error: should be assertFalse(habit.completed_today)
        self.assertEqual(habit.completed_today, False)

    def test_update_streak_completed(self):
        self.habit.completed_today = True
        self.habit.update_streak()
        # Error: should be self.assertEqual(self.habit.streak, 1)
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
