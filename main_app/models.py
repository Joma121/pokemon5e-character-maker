from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.email

# Ability Stats > Strength, Constitution, Wisdom, etc
class Ability(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

# DND Skills > Athletics, Stealth, Insight, etc
class Skill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
# Languages > Hinoan, Common, etc
class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
# Pokemon Type > Grass, Fire, Dragon, etc
class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
    
# Pokemon moves > Scratch, Ember, Vine Whip, etc
class Move(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

class EggGroup(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['name']

class PokemonAbility(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=200)
    is_hidden = models.BooleanField()

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=700)
    strength_bonus = models.IntegerField()
    dexterity_bonus = models.IntegerField()
    constitution_bonus = models.IntegerField()
    wisdom_bonus = models.IntegerField()
    intelligence_bonus = models.IntegerField()
    charisma_bonus = models.IntegerField()
    languages = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class RaceFeature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    short_description = models.TextField(max_length=200)
    is_skill_proficiency = models.BooleanField()
    is_ability_bonus = models.BooleanField()
    modifies = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class TrainerClass(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField(default=1)
    hit_dice = models.IntegerField(default=8)
    proficiency_bonus = models.IntegerField()
    pokeslots = models.IntegerField()
    max_specie_rating = models.IntegerField()
    skill_proficiencies = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name

class ClassFeature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    level_acquired = models.IntegerField()
    trainer_class = models.ForeignKey(TrainerClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['id']

class Specialization(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    ability = models.ManyToManyField(Ability)
    skill = models.ManyToManyField(Skill)
    bonus_value = models.IntegerField()
    is_other_bonus = models.BooleanField()
    pokemon_type = models.ForeignKey(PokemonType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# class TrainerPath(models.Model):
#     name = models.CharField(max_length=25)
#     description = models.TextField(max_length=700)
#     short_description = models.TextField(max_length=200)
#     first_feature_name = models.CharField(max_length=25)
#     first_description = models.TextField(max_length=700)
#     first_short_description = models.TextField(max_length=200)
#     second_feature_name = models.CharField(max_length=25)
#     second_description = models.TextField(max_length=700)
#     second_short_description = models.TextField(max_length=200)
#     third_feature_name = models.CharField(max_length=25)
#     third_description = models.TextField(max_length=700)
#     third_short_description = models.TextField(max_length=200)

#     def __str__(self):
#         return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    description = models.TextField(max_length=500)
    classification = models.CharField(max_length=30)
    specie_rating = models.CharField(max_length=5)
    male_rate = models.IntegerField()
    female_rate = models.IntegerField()
    evolution_stage = models.IntegerField()
    max_evolution_stage = models.IntegerField()
    ability_score_increase = models.IntegerField()
    armor_class = models.IntegerField()
    average_hit_points = models.IntegerField()
    hit_dice = models.IntegerField()
    walking_speed = models.IntegerField()
    flying_speed = models.IntegerField()
    swimming_speed = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    can_evolve = models.BooleanField()
    evolution_description = models.TextField(max_length=600)
    pokemon_type = models.ManyToManyField(PokemonType)
    egg_group = models.ManyToManyField(EggGroup)
    proficient_skills = models.ManyToManyField(Skill)
    ability_saving_throws = models.ManyToManyField(Ability)
    vulnerability_type = models.ManyToManyField(PokemonType, related_name='vulnerable_type')
    resistance_types = models.ManyToManyField(PokemonType, related_name='resistant_type')
    starting_moves = models.ManyToManyField(Move)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ['number']

class Character(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField()
    alignment = models.CharField(max_length=20, blank=True)
    lifestyle = models.CharField(max_length=60, blank=True)
    hair = models.TextField(max_length=300, blank=True)
    skin = models.TextField(max_length=300, blank=True)
    eyes = models.TextField(max_length=300, blank=True)
    height = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    age = models.CharField(max_length=30, blank=True)
    notes = models.TextField(max_length=1000, blank=True)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    trainer_license = models.BooleanField()
    pokedex = models.BooleanField()
    pokeballs = models.IntegerField()
    potions = models.IntegerField()
    pokedollars = models.IntegerField()
    pack = models.CharField(max_length=30)
    skill_one = models.ForeignKey(Skill, related_name="skill_one", on_delete=models.SET_NULL, null=True)
    skill_two = models.ForeignKey(Skill, related_name="skill_two", on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    trainer_class = models.ForeignKey(TrainerClass, on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    # path = models.ForeignKey(TrainerPath, on_delete=models.SET_NULL, null=True)
    starter_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
