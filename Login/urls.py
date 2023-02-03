from django.urls import path
from . import views

app_name="Login"
urlpatterns = [
    path("",views.LoginUsers,name="LoginUser"),
    path("Admin/",views.LoginAdmins,name="LoginAdmin"),
    path("<str:nom><int:ListeUser>",views.Operations,name="Operations"),
]