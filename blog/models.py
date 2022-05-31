from django.db import models
from user.models import UserModel
from taggit.managers import TaggableManager


class CategoryModel(models.Model):
    class Meta:
        db_table = "category"

    category = models.CharField(max_length=256)


class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
