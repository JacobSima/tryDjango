from django.urls import path
from .views import (
  BlogListView,
  BlogDetailView,
  BlogCreateView,
  BlogUpdateView,
  BlogDeleteView
)

app_name = 'blogs'
urlpatterns = [
  path('',BlogListView.as_view(),name='blogs_list'),
  path('<int:id>/',BlogDetailView.as_view(),name='detail_view'),
  path('create/',BlogCreateView.as_view(),name='create_view'),
  path('<int:id>/update/',BlogUpdateView.as_view(),name='update_view'),
  path('<int:id>/delete/',BlogDeleteView.as_view(),name='delete_view')
]