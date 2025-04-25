from bson import ObjectId
from djongo import models

class ObjectIdField(models.Field):
    def get_prep_value(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def from_db_value(self, value, expression, connection):
        if not value:
            return None
        return ObjectId(value)

class User(models.Model):
    id = ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()