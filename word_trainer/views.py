from rest_framework import viewsets
from .models import Dictionary, Word
from .serializers import DictionarySerializer, WordSerializer


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer