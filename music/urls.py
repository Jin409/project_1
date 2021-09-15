from django.urls import path
from . import views

app_name = 'music'

urlpatterns=[
    path('rain/',views.rain,name="rain"),
    path('<int:id>',views.detail,name="detail"),
    path('list/',views.list,name="list"),

    
]