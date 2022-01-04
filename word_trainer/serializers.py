from rest_framework import serializers
from .models import Dictionary, Word
from django.contrib.auth.models import User


class DictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = ['id', 'owner', 'dictionary_name', 'get_words_count', 'date_created']


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['id', 'dictionary', 'word_rus', 'word_eng']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
