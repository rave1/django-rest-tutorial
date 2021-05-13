from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('people/', views.SnippetList.as_view()),
    path('people/<int:pk>/', views.SnippetDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
