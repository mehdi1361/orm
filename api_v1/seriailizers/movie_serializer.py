from rest_framework import serializers
from movie.models import Film, FilmActor, FilmCategory

class FilmActorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='actor.id')
    name = serializers.ReadOnlyField(source='actor.name')

    class Meta:
        model = FilmActor
        fields = ['id', 'name']


class FilmCategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='category.id')
    name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = FilmCategory
        fields = ['id', 'name', 'last_update']


class FilmSerializer(serializers.ModelSerializer):

    categores = FilmCategorySerializer(source='filmcategory_set', many=True)
    language_name = serializers.CharField(source='language.name')
    director_name = serializers.CharField(source='director.name')
    actor_name = FilmActorSerializer(source='filmactor_set')

    class Meta:
        model = Film
        fields = ['title', 'description', 'release_year',
                  'rental_duration', 'rental_rate', 'length', 'director_name', 'actor_name',
                  'replacement_cost', 'rating', 'cover', 'language_name', 'fa_title', 'categores']
