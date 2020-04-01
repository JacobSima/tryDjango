from django.shortcuts import render,get_object_or_404,redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_list_view(request):
  obj = Article.objects.all()
  context ={
    'object':obj
  }
  return render(request,'articles/article_list.html', context)


def article_detail_view(request,id):
  obj = get_object_or_404(Article,pk = id)
  context ={
    'object':obj
  }
  return render(request, 'articles/article_detail.html',context)



def article_create_view(request):
  form = ArticleForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ArticleForm()
  context ={
    'form':form
  }
  return render(request,'articles/article_create.html',context)


