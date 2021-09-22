from django.urls import path
from . import views

app_name = 'music'

urlpatterns=[
    path('rain/',views.rain,name="rain"),
    path('<int:id>/',views.detail,name="detail"),
    path('list/',views.list,name="list"),
    path('sunny/',views.sunny,name="sunny"),
    path('christmas/',views.christmas,name="christmas"),
    path('midnight/',views.midnight,name="midnight"),
    path('create/',views.create,name="create"),
    path('new/',views.new,name="new"),
    path('<int:id>/delete/',views.delete,name="delete"),
    path('comment/<int:id>/delete/',views.comment_delete,name="comment_delete"),
  


    
]