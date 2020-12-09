from django.db import models

# Create your models here.

class List(models.Model):
    listName = models.CharField(max_length=100,verbose_name="List Name")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.listName

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'