from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Count, Sum
from .models import User, Course, Enrollment, Payment

def admin_dashboard(request):
    total_users = User.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    total_revenue = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0

    # Course popularity
    popular_courses = (
        Enrollment.objects
        .values('course__title')
        .annotate(total=Count('id'))
    )

    course_labels = [c['course__title'] for c in popular_courses]
    course_data = [c['total'] for c in popular_courses]

    context = {
        "total_users": total_users,
        "total_courses": total_courses,
        "total_enrollments": total_enrollments,
        "total_revenue": total_revenue,
        "course_labels": course_labels,
        "course_data": course_data,
    }

    return render(request, "admin_dashboard.html", context)