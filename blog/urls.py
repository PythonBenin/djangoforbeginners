from django.urls import path

from .views import BlogDeleteView
from .views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateView  # noqa: E501

urlpatterns = [
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),  # noqa: E501
    path("post/new/", BlogCreateView.as_view(), name="post_new"),  # noqa: E501
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),  # noqa: E501
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),  # noqa: E501
    path("", BlogListView.as_view(), name="home"),  # noqa: E501
    path("", BlogListView.as_view(), name="home"),  # noqa: E501
]
