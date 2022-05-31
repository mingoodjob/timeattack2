from django.contrib import admin
from .models import CategoryModel
from .models import ArticleModel


# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ArticleModel)