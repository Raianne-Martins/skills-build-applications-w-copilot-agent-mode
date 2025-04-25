from datetime import timedelta

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Test data for users
        user1 = User.objects.create(username="john_doe", email="john@example.com", password="password123")
        user2 = User.objects.create(username="jane_doe", email="jane@example.com", password="password123")

        # Test data for teams
        team1 = Team.objects.create(name="Team Alpha", members=["john_doe", "jane_doe"])
        team2 = Team.objects.create(name="Team Beta", members=["jane_doe"])

        # Test data for activities
        Activity.objects.create(user=user1, activity_type="Running", duration=timedelta(minutes=30))
        Activity.objects.create(user=user2, activity_type="Cycling", duration=timedelta(hours=1))

        # Test data for leaderboard
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Test data for workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session to start your day.")
        Workout.objects.create(name="HIIT", description="High-intensity interval training for fat burning.")

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
