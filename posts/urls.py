from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.index,name='index'),
    path('cbv/',views.CBView.as_view()),
    path('cbv_index/',views.IndexView.as_view()),
    path('list/',views.SchoolListView.as_view()),
    path('<int:pk>/',views.SchoolDetailView.as_view()),
]