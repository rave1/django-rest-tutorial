from django.urls import path
from api import views

urlpatterns = [
    path('people/', views.people_list),
    path('people/<int:pk>/', views.people_detail)
]