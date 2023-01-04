from .import views
from django.urls import path




urlpatterns = [ 
    
    path('<int:id>', views.index, name='index'),
    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path("home",views.home, name="home"),
    path("view/", views.view, name="view"),
    path("list/", views.list, name="list"),


]






