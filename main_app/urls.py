from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.all_characters, name="all_characters"),
    path('characters/my', views.my_characters, name="my_characters"),
    path('characters/new', views.new_character, name="new_character"),
    path('account/signup', views.signup, name="signup"),
    path('account/login', views.login, name="login"),
    path('account/logout', views.logout, name="logout"),

]