from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    # Home page with latest articles
    path("", views.ArticleListView.as_view(), name="home"),
    
    # Article detail page
    path("article/<slug:slug>/", views.article_detail, name="article_detail"),

    # Search functionality
    path("search/", views.search_articles, name="search_articles"),
]
