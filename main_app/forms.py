from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Character

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CharacterCreationForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('skill_one','skill_two','name', 'alignment', 'lifestyle', 'hair', 'skin', 'eyes', 'height', 'weight', 'age', 'notes', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'trainer_license', 'pokedex', 'pokeballs', 'potions', 'pokedollars', 'pack', 'race', 'specialization', 'starter_pokemon')