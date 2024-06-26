from django.urls import path # type: ignore
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns # type: ignore

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)