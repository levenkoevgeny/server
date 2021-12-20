from django.db import models


class Dictionary(models.Model):
    dictionary_name = models.CharField(max_length=255, verbose_name="Dictionary name")

    def __str__(self):
        return self.dictionary_name

    class Meta:
        ordering = ('dictionary_name',)
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="Dictionary")
    word_rus = models.CharField(max_length=255, verbose_name="Word(rus)")
    word_eng = models.CharField(max_length=255, verbose_name="Word(eng)")

    def __str__(self):
        return self.word_rus + ' ' + self.word_eng

    class Meta:
        ordering = ('word_rus',)
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
