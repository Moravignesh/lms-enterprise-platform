from fastapi import FastAPI
from routers import (
    auth,
    plans,
    courses,
    subscription,
    payments,
    progress,
    notifications,
    analytics,
    activity,
)

app = FastAPI(title="LMS Enterprise API")

# AUTH
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# LMS
app.include_router(courses.router, tags=["Courses"])
app.include_router(progress.router, tags=["Progress"])

# SUBSCRIPTION
app.include_router(plans.router, tags=["Plans"])
app.include_router(subscription.router, tags=["Subscription"])
app.include_router(payments.router, tags=["Payments"])

# NOTIFICATIONS
app.include_router(notifications.router, tags=["Notifications"])

# ANALYTICS
app.include_router(analytics.router, tags=["Analytics"])
app.include_router(activity.router, tags=["Activity"])




app.include_router(notifications.router)
app.include_router(activity.router)