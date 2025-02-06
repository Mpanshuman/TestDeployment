from django.db import models


# Create your models here.


class BaseDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseDateModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(BaseDateModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
