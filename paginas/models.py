from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(
    max_length=255,
    verbose_name='Nome')

    email = models.EmailField(
    max_length=255,
    verbose_name='E-mail')

    comentario = models.CharField(
    max_length=1200,
    verbose_name='Comentário')

    def __str__(self):
        return self.nome + ' ' + self.email