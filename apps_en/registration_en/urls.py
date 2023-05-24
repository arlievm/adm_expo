from django.urls import path
from .views import ApplicationCreateListView, ApplicationDeleteView


urlpatterns = [
    ############   Заявка
    path('application-en/', ApplicationCreateListView.as_view()),
    path('application-en/<int:pk>', ApplicationDeleteView.as_view()),
]