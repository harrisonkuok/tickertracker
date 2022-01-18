from django.urls import path
from .views import CustomUserCreate, UserSettings

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('settings/', UserSettings.as_view(), name="settings")
]
