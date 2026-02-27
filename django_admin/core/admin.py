from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Progress)
admin.site.register(Subscription)
admin.site.register(Payment)

admin.site.register(Notification)
admin.site.register(ActivityLog)
admin.site.register(AnalyticsRecord)