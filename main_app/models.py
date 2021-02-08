from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# Ability Stats > Strength, Constitution, Wisdom, etc
class Ability(models.Model):
    name = models.CharField(max_length=20)

# DND Skills > Athletics, Stealth, Insight, etc
class Skill(models.Model):
    name = models.CharField(max_length=20)
    
# Languages > Hinoan, Common, etc
class Language(models.Model):
    name = models.CharField(max_length=20)
    
# Pokemon Type > Grass, Fire, Dragon, etc
class PokemonType(models.Model):
    name = models.CharField(max_length=20)
    
# Pokemon moves > Scratch, Ember, Vine Whip, etc
class Move(models.Model):
    name = models.CharField(max_length=20)


class RaceFeature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=200)
    is_skill_proficiency = models.BooleanField
    is_ability_bonus = models.BooleanField
    modifies = models.CharField(max_length=100)
    modify_value = models.IntegerField


class ClassFeature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    level_acquired = models.IntegerField


class PokemonAbility(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=200)
    is_hidden = models.BooleanField

class Race(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    strength_bonus = models.IntegerField
    dexterity_bonus = models.IntegerField
    constitution_bonus = models.IntegerField
    wisdom_bonus = models.IntegerField
    intelligence_bonus = models.IntegerField
    charisma_bonus = models.IntegerField
    ability_bonus_name = models.CharField(max_length=20)
    race_feature = models.ForeignKey(RaceFeature, on_delete=models.SET_NULL, null=True)
    languages = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


class TrainerClass(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField(default=1)
    hit_dice = models.IntegerField(default=8)
    skill_proficiencies = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    proficiency_bonus = models.IntegerField
    features = models.ForeignKey(ClassFeature, on_delete=models.SET_NULL, null=True)
    pokeslots = models.IntegerField
    max_specie_rating = models.IntegerField

class Specialization(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    pokemon_type = models.ForeignKey(PokemonType, on_delete=models.SET_NULL, null=True)
    ability = models.ForeignKey(Ability, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    bonus_value = models.IntegerField
    is_other_bonus = models.BooleanField

class TrainerPath(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=200)
    first_feature_name = models.CharField(max_length=20)
    first_description = models.TextField(max_length=500)
    first_short_description = models.TextField(max_length=200)
    second_feature_name = models.CharField(max_length=20)
    second_description = models.TextField(max_length=500)
    second_short_description = models.TextField(max_length=200)
    third_feature_name = models.CharField(max_length=20)
    third_description = models.TextField(max_length=500)
    third_short_description = models.TextField(max_length=200)

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField
    description = models.TextField(max_length=500)
    pokemon_type = models.ForeignKey(PokemonType, on_delete=models.SET_NULL, null=True)
    classification = models.CharField(max_length=30)
    specie_rating = models.CharField(max_length=5)
    egg_group = models.ForeignKey(PokemonType, related_name='egg_type', on_delete=models.SET_NULL, null=True)
    male_rate = models.IntegerField
    female_rate = models.IntegerField
    evolution_stage = models.IntegerField
    max_evolution_stage = models.IntegerField
    ability_score_increase = models.IntegerField
    armor_class = models.IntegerField
    average_hit_points = models.IntegerField
    hit_dice = models.IntegerField
    walking_speed = models.IntegerField
    flying_speed = models.IntegerField
    swimming_speed = models.IntegerField
    strength = models.IntegerField
    dexterity = models.IntegerField
    constitution = models.IntegerField
    intelligence = models.IntegerField
    wisdom = models.IntegerField
    charisma = models.IntegerField
    proficient_skills = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    ability_saving_throws = models.ForeignKey(Ability, on_delete=models.SET_NULL, null=True)
    vulnerability_type = models.ForeignKey(PokemonType, related_name='vulnerable_type', on_delete=models.SET_NULL, null=True)
    resistance_types = models.ForeignKey(PokemonType, related_name='resistant_type', on_delete=models.SET_NULL, null=True)
    can_evolve = models.BooleanField
    evolution_description = models.TextField(max_length=500)
    starting_moves = models.ForeignKey(Move, on_delete=models.SET_NULL, null=True)

class CharacterItem(models.Model):
    trainer_license = models.BooleanField
    pokedex = models.BooleanField
    pokeballs = models.IntegerField
    potions = models.IntegerField
    pokedollars = models.IntegerField
    pack = models.CharField(max_length=30)

class Character(models.Model):
    name = models.CharField(max_length=20)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField
    alignment = models.CharField(max_length=20)
    lifestyle = models.CharField(max_length=60)
    hair = models.TextField(max_length=300)
    skin = models.TextField(max_length=300)
    eyes = models.TextField(max_length=300)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    age = models.CharField(max_length=30)
    notes = models.TextField(max_length=1000)
    skill_proficiencies = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    proficiency_bonus = models.IntegerField
    features = models.ForeignKey(ClassFeature, on_delete=models.SET_NULL, null=True)
    pokeslots = models.IntegerField
    max_specie_rating = models.IntegerField
    items = models.OneToOneField(CharacterItem, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    path = models.OneToOneField(TrainerPath, on_delete=models.SET_NULL, null=True)
    strength = models.IntegerField
    dexterity = models.IntegerField
    constitution = models.IntegerField
    intelligence = models.IntegerField
    wisdom = models.IntegerField
    charisma = models.IntegerField
    starter_pokemon = models.OneToOneField(Pokemon, on_delete=models.SET_NULL, null=True)

class CustomUser(AbstractUser):
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.email