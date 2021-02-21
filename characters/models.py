from django.db import models

class NPC(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    titulo = models.CharField(max_length=50, blank=True)
    idade = models.PositiveIntegerField(blank=False)
    raca = models.CharField(max_length=20, blank=False)
    classe = models.CharField(max_length=20, blank=False)
    historia = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    


