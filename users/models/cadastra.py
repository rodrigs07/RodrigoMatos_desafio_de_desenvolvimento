from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    cargo = models.CharField(max_length=25)

    def __str__(self):
        return ("nome %s, cargo %s" %(self.nome, self.cargo))


