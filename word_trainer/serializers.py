from rest_framework import serializers
from .models import Dictionary, Word


class DictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ['dictionary', 'word_rus', 'word_eng']