from django.urls import path
from .views import home,CourseView,CourseCreateView,CourseUpdateView,CourseDeleteView


app_name = 'Courses'
urlpatterns  = [
#  path('',home,name='courses'),
 path('',CourseView.as_view(),name='courses'),
#  path('',CourseView.as_view(template_name = 'delete.html'),name='courses'),
 path('<int:id>/',CourseView.as_view(),name='course_detail'),
 path('create/',CourseCreateView.as_view(),name='course_create'),
 path('<int:id>/update/', CourseUpdateView.as_view(),name='course_update'),
 path('<int:id>/delete/', CourseDeleteView.as_view(),name='course_delete'),
]