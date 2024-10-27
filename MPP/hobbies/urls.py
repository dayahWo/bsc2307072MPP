from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path('newmentor', views.newmentor, name="newmentor"),
path('newstudent', views.newstudent, name="newstudent"),
path('update/<str:menid>',views.update, name='update'),
path('update/updatedata/<str:menid>',views.updatedata,name='updatedata'),
path('viewdelete/<str:menid>',views.viewdelete, name='viewdelete'),
path('viewdelete/deletedata/<str:menid>',views.delete, name='delete'),
path("searchpage", views.searchpage, name="searchpage"),
]