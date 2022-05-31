from django.shortcuts import render, redirect
from .models import CategoryModel
from .models import ArticleModel


def home(request):
    if request.method == 'GET':
        article = ArticleModel.objects.all()
        category = CategoryModel.objects.all()
        return render(request, 'index.html', {'article': article, 'category': category})


def article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title, content)
        data = ArticleModel()
        data.title = request.POST.get('title')
        data.content = request.POST.get('content')
        data.category = request.POST.get('category')
        data.save()

    return redirect('/')
