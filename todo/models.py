from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=100,verbose_name="List Name")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'

class ListItem(models.Model):
    name = models.CharField(max_length=100,verbose_name="Item Name")
    explanation = models.CharField(max_length=100,verbose_name="Item Explanation")
    deadline = models.DateTimeField(verbose_name='Item Deadline')
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name="Item Created Date")
    status = models.BooleanField(verbose_name='is Complete?')
    tList = models.ForeignKey(List, on_delete=models.CASCADE,verbose_name='List')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo List Item'
        verbose_name_plural = 'Todo List Items'