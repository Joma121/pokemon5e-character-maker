# Generated by Django 3.1.6 on 2021-02-09 00:51

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_license', models.BooleanField()),
                ('pokedex', models.BooleanField()),
                ('pokeballs', models.IntegerField()),
                ('potions', models.IntegerField()),
                ('pokedollars', models.IntegerField()),
                ('pack', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ClassFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=600)),
                ('level_acquired', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('short_description', models.TextField(max_length=200)),
                ('is_hidden', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RaceFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('short_description', models.TextField(max_length=200)),
                ('is_skill_proficiency', models.BooleanField()),
                ('is_ability_bonus', models.BooleanField()),
                ('modifies', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('short_description', models.TextField(max_length=200)),
                ('first_feature_name', models.CharField(max_length=20)),
                ('first_description', models.TextField(max_length=500)),
                ('first_short_description', models.TextField(max_length=200)),
                ('second_feature_name', models.CharField(max_length=20)),
                ('second_description', models.TextField(max_length=500)),
                ('second_short_description', models.TextField(max_length=200)),
                ('third_feature_name', models.CharField(max_length=20)),
                ('third_description', models.TextField(max_length=500)),
                ('third_short_description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('level', models.IntegerField(default=1)),
                ('hit_dice', models.IntegerField(default=8)),
                ('proficiency_bonus', models.IntegerField()),
                ('pokeslots', models.IntegerField()),
                ('max_specie_rating', models.IntegerField()),
                ('features', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.classfeature')),
                ('skill_proficiencies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('bonus_value', models.IntegerField()),
                ('is_other_bonus', models.BooleanField()),
                ('ability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.ability')),
                ('pokemon_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.pokemontype')),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=700)),
                ('strength_bonus', models.IntegerField()),
                ('dexterity_bonus', models.IntegerField()),
                ('constitution_bonus', models.IntegerField()),
                ('wisdom_bonus', models.IntegerField()),
                ('intelligence_bonus', models.IntegerField()),
                ('charisma_bonus', models.IntegerField()),
                ('languages', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.language')),
                ('race_feature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.racefeature')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('classification', models.CharField(max_length=30)),
                ('specie_rating', models.CharField(max_length=5)),
                ('male_rate', models.IntegerField()),
                ('female_rate', models.IntegerField()),
                ('evolution_stage', models.IntegerField()),
                ('max_evolution_stage', models.IntegerField()),
                ('ability_score_increase', models.IntegerField()),
                ('armor_class', models.IntegerField()),
                ('average_hit_points', models.IntegerField()),
                ('hit_dice', models.IntegerField()),
                ('walking_speed', models.IntegerField()),
                ('flying_speed', models.IntegerField()),
                ('swimming_speed', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('can_evolve', models.BooleanField()),
                ('evolution_description', models.TextField(max_length=500)),
                ('ability_saving_throws', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.ability')),
                ('egg_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='egg_type', to='main_app.pokemontype')),
                ('pokemon_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.pokemontype')),
                ('proficient_skills', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.skill')),
                ('resistance_types', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resistant_type', to='main_app.pokemontype')),
                ('starting_moves', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.move')),
                ('vulnerability_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vulnerable_type', to='main_app.pokemontype')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('alignment', models.CharField(max_length=20)),
                ('lifestyle', models.CharField(max_length=60)),
                ('hair', models.TextField(max_length=300)),
                ('skin', models.TextField(max_length=300)),
                ('eyes', models.TextField(max_length=300)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=30)),
                ('notes', models.TextField(max_length=1000)),
                ('proficiency_bonus', models.IntegerField()),
                ('pokeslots', models.IntegerField()),
                ('max_specie_rating', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('features', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.classfeature')),
                ('items', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.characteritem')),
                ('path', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.trainerpath')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.race')),
                ('skill_proficiencies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.skill')),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.specialization')),
                ('starter_pokemon', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.character')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
