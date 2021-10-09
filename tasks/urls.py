from django.urls import path 
from . import views

app_name = "tasks"

urlpatterns = [
    path("" , views.index , name="index") , 
    path("add" , views.add , name = "add"),
    path("delete/<str:name>",views.delete , name="delete") , 
    path("clear" , views.clear , name="clear")

]