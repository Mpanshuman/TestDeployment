from django.urls import path
from .views import *

urlpatterns = [
    path("article/", ArticleListCreateView.as_view()),
    path("article/<int:pk>/", ArticleUpdateDeleteView.as_view()),
    path("author/", AuthorListCreateView.as_view()),
    path("author/<int:pk>/", AuthorUpdateDeleteView.as_view()),
]
