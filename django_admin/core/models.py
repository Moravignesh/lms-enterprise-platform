from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models


class User(models.Model):
    ROLE_CHOICES = (
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("admin", "Admin"),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# -------------------------
# SUBSCRIPTION PLAN
# -------------------------
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name


# -------------------------
# COURSE
# -------------------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -------------------------
# LESSON
# -------------------------
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title


# -------------------------
# ENROLLMENT
# -------------------------
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)


# -------------------------
# PROGRESS TRACKING
# -------------------------
class Progress(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    completed_lessons = models.IntegerField(default=0)
    progress_percent = models.FloatField(default=0)


# -------------------------
# SUBSCRIPTION
# -------------------------
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)


# -------------------------
# PAYMENT
# -------------------------
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    user = models.ForeignKey("core.User", on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    action_detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class AnalyticsRecord(models.Model):
    date = models.DateField()
    total_users = models.IntegerField()
    active_subscriptions = models.IntegerField()
    revenue = models.FloatField()
    popular_course = models.CharField(max_length=200)