from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Ability, Skill, Language, PokemonType, Move, RaceFeature, ClassFeature, PokemonAbility, Race, TrainerClass, Specialization, TrainerPath, Pokemon, Character, EggGroup
from .forms import CustomUserCreationForm, CustomUserChangeForm, CharacterCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def all_characters(request):
    return render(request, 'characters/all_characters.html')

@login_required
def my_characters(request):
    return render(request, 'characters/my_characters.html')

@login_required
def new_character(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        character_form = CharacterCreationForm(request.POST, request.FILES)
        if character_form.is_valid():
            new_character = character_form.save(commit=false)
            new_character.user = user

    character_form = CharacterCreationForm()
    languages = Language.objects.all()
    abilities = Ability.objects.all()
    skills = Skill.objects.all()

    races = Race.objects.select_related()
    raceFeatures = RaceFeature.objects.select_related()

    trainer = TrainerClass.objects.get(id=1)
    trainerFeatures = ClassFeature.objects.all()
    specializations = Specialization.objects.prefetch_related('skill').select_related('pokemon_type')
    trainerPaths = TrainerPath.objects.all()

    pokemonTypes = PokemonType.objects.all()
    pokemonAbilities = PokemonAbility.objects.all()
    eggGroups = EggGroup.objects.all()
    pokemon = Pokemon.objects.all()

    context = {
        'languages': languages,
        'abilities': abilities,
        'skills': skills,
        'races': races,
        'raceFeatures': raceFeatures,
        'trainer': trainer,
        'trainerFeatures': trainerFeatures,
        'trainerPaths': trainerPaths,
        'specializations': specializations,
        'pokemonTypes': pokemonTypes,
        'pokemonAbilities': pokemonAbilities,
        'eggGroups': eggGroups,
        'pokemons': pokemon,
        'character_form': character_form,
    }
    print (trainer)
    return render(request, 'characters/new_character.html', context)
    