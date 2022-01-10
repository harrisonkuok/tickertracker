from django.urls import path
from tickertrackerapp import views

urlpatterns = [
    path('api/stocks/top', views.stock_mentions_ranking)
]

