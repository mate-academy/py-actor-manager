from django.db import models  # Import correto para usar Model e campos

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        # Retorna o nome completo do ator para facilitar a visualização
        return f"{self.first_name} {self.last_name}"
