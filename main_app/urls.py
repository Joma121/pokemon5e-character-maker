from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.my_characters, name="my_characters"),
    path('characters/new', views.new_character, name="new_character"),
    path('characters/edit/<int:char_id>', views.edit_character, name="edit_character"),
    path('characters/delete/<int:char_id>', views.delete_character, name="delete_character"),
    path('characters/<int:char_id>', views.show_character, name="show_character"),

]