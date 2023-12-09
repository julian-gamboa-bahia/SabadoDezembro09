from django.db import models

class Imagens(models.Model):
    id = models.AutoField(primary_key=True)
    caminho = models.TextField()
    conteudo = models.BinaryField()