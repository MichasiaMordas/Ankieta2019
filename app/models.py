from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Uzytkownik(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    wiek = models.CharField(max_length=50)
    plec = models.CharField(max_length=20, default="0")
    miasto = models.CharField(max_length=100)
    wyksztalcenie = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)


class Czestosc(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    okazja = models.CharField(max_length=200)
    czestotliwosc = models.CharField(max_length=200)
    pierwszy_kontakt = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

class Alkohol(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rodzaj_alkoholu = models.CharField(max_length=200)
    piwo = models.CharField(max_length=100)
    wodka = models.CharField(max_length=100)
    wino = models.CharField(max_length=100)
    inne = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)