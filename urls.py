from timetable_app.views import (
    generatetimetable, home, loginvalidation, oddevensemselect, 
    subjectadded, facultyadded, loadallocation, subjectselect, facultyselect
)
from django.urls import path  # use path or re_path
from . import views
from .views import home
urlpatterns = [
    path('home/', views.home, name='home'),
    path('loginvalidation/', views.loginvalidation, name='loginvalidation'),
    path('oddevensemselect/', views.oddevensemselect, name='oddevensemselect'),
    path('subjectadded/', views.subjectadded, name='subjectadded'),
    path('facultyadded/', views.facultyadded, name='facultyadded'),
    path('subjectselect/', views.subjectselect, name='subjectselect'),
    path('facultyselect/', views.facultyselect, name='facultyselect'),
    path('loadallocation/', views.loadallocation, name='loadallocation'),
    path('generatetimetable/', views.generatetimetable, name='generatetimetable'),
     path('', home, name='home'), # default home path
]

