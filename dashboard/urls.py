from django.urls import path
from .views import Dashboard, FeedbackForm

urlpatterns = [
    path('', Dashboard, name='dashboard'),
    path('/dashboard', Dashboard, name='dashboard'),
    path("feedback/<lat>/<lng>", FeedbackForm)
]