from django.db import models

# Create your models here.
class Skills(models.Model):
    title = models.CharField(max_length=30)
    count_skill = models.IntegerField()

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Ключевые навыки'

    def __str__(self):
        return self.title
