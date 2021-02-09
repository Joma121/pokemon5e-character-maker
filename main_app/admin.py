from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Ability, Skill, Language, PokemonType, Move, RaceFeature, ClassFeature, PokemonAbility, Race, TrainerClass, Specialization, TrainerPath, Pokemon, CharacterItem, Character

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Ability)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(PokemonType)
admin.site.register(Move)
admin.site.register(RaceFeature)
admin.site.register(ClassFeature)
admin.site.register(PokemonAbility)
admin.site.register(Race)
admin.site.register(TrainerClass)
admin.site.register(Specialization)
admin.site.register(TrainerPath)
admin.site.register(Pokemon)
admin.site.register(CharacterItem)
admin.site.register(Character)