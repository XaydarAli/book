from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=100)
    count=models.PositiveIntegerField()
    price=models.FloatField()
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Author(models.Model):
    full_name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    nationality=models.CharField(max_length=100)
    genre=models.CharField(max_length=25)
    email_address=models.CharField(max_length=50)
    def __str__(self):
        return self.full_name

