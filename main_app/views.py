from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Ability, Skill, Language, PokemonType, Move, RaceFeature, ClassFeature, PokemonAbility, Race, TrainerClass, Specialization, Pokemon, Character, EggGroup
from .forms import CustomUserCreationForm, CustomUserChangeForm, CharacterCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def my_characters(request):
    characters = Character.objects.filter(user_id=request.user.id)
    context = {'characters': characters}
    return render(request, 'characters/my_characters.html', context)

@login_required
def new_character(request):
    user = CustomUser.objects.get(id=request.user.id)
    trainer_class = TrainerClass.objects.get(id=1)
    level = 1
    if request.method == 'POST':
        character_form = CharacterCreationForm(request.POST)
        print(character_form)
        if character_form.is_valid():
            new_character = character_form.save(commit=False)
            new_character.user = user
            new_character.level = level
            new_character.trainer_class = trainer_class
            new_character.save()
            return redirect('my_characters')

    character_form = CharacterCreationForm()
    races = Race.objects.select_related()
    raceFeatures = RaceFeature.objects.select_related()
    trainerFeatures = ClassFeature.objects.all()
    specializations = Specialization.objects.all()
    pokemon = Pokemon.objects.all()
    
    context = {
        'races': races,
        'raceFeatures': raceFeatures,
        'trainerFeatures': trainerFeatures,
        'specializations': specializations,
        'pokemons': pokemon,
        'character_form': character_form,
    }
    return render(request, 'characters/new_character.html', context)

def show_character(request, char_id):
    character = Character.objects.get(id=char_id)
    race = Race.objects.get(id=character.race.id)
    racefeatures = RaceFeature.objects.select_related('race')
    trainerfeatures = ClassFeature.objects.all()
    languages = Language.objects.all()
    specializations = Specialization.objects.all()
    pokemon = Pokemon.objects.get(id=character.starter_pokemon.id)

    context = {
        'character': character,
        'race': race,
        'racefeatures': racefeatures,
        'trainerfeatures': trainerfeatures,
        'languages': languages,
        'specializations': specializations,
        'starter': pokemon,
    }
    return render(request, 'characters/show_character.html', context)

def edit_character(request, char_id):
    character = Character.objects.get(id=char_id)

    if request.method == 'POST':
        character_form = CharacterCreationForm(request.POST, instance=character)
        if character_form.is_valid():
            character_form.save()
            return redirect('my_characters')

    character_form = CharacterCreationForm(instance=character)
    races = Race.objects.select_related()
    raceFeatures = RaceFeature.objects.select_related()
    trainerFeatures = ClassFeature.objects.all()
    specializations = Specialization.objects.all()
    pokemon = Pokemon.objects.all()
    if character_form.errors:
        print(character_form.errors)
    context = {
        'races': races,
        'raceFeatures': raceFeatures,
        'trainerFeatures': trainerFeatures,
        'specializations': specializations,
        'pokemons': pokemon,
        'character_form': character_form,
        'character': character,
    }
    return render(request, 'characters/edit_character.html', context)

def delete_character(request, char_id):
    character = Character.objects.get(id=char_id)
    character.delete()
    return redirect("my_characters")
