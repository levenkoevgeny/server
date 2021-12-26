from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Dictionary(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    dictionary_name = models.CharField(max_length=255, verbose_name="Dictionary name")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.dictionary_name

    @property
    def get_words_count(self):
        return self.word_set.all().count()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, verbose_name="Dictionary")
    word_rus = models.CharField(max_length=255, verbose_name="Word(rus)")
    word_eng = models.CharField(max_length=255, verbose_name="Word(eng)")
    is_trouble = models.BooleanField(verbose_name="Word with trouble", default=False)

    def __str__(self):
        return self.word_rus + ' ' + self.word_eng

    class Meta:
        ordering = ('word_rus',)
        verbose_name = 'Word'
        verbose_name_plural = 'Words'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
