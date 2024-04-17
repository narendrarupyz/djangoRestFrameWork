from django.urls import path # type: ignore
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns # type: ignore

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)