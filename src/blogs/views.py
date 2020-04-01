from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)
from .models import Blog
from .forms import BlogModelForm

# Create your views here.

class BlogListView(ListView):
  template_name = 'blogs/blogs_list.html'
  queryset = Blog.objects.all()   # this is a requirement 


 
class BlogDetailView(DetailView):
  template_name = 'blogs/blogs_detail.html'
  queryset = Blog.objects.all()   # this is a requirement 

  # Build in with class base view especially with detail view
  # we use this, in order to use the id on the url instead of pk
  def get_object(self):   # a function that only works for class base view
    id_ = self.kwargs.get('id')    # What is passed in the url. eg : /blogs/1
    return get_object_or_404(Blog, id=id_)



class BlogCreateView(CreateView):
  template_name = 'blogs/blogs_create.html'
  form_class = BlogModelForm
  queryset = Blog.objects.all()

  # success_url = '/'      # another way to redirect after form submittion 

  def form_valid(self,form):    # this allow us to see which data is coming
    print(form.cleaned_data)
    return super().form_valid(form)

  # def get_success_url(self):
  #   return '/'




class BlogUpdateView(UpdateView):
  template_name = 'blogs/blogs_create.html'
  form_class = BlogModelForm
  queryset = Blog.objects.all()

  # success_url = '/'      # another way to redirect after form submittion 

  def get_object(self):
    id_ = self.kwargs['id']
    return get_object_or_404(Blog,id=id_)

  def form_valid(self,form):    # this allow us to see which data is coming
    print(form.cleaned_data)
    return super().form_valid(form)


  # def get_success_url(self):
  #   return '/'





 
class BlogDeleteView(DeleteView):
  template_name = 'blogs/blogs_delete.html'
 
  def get_object(self):   # a function that only works for class base view
    id_ = self.kwargs.get('id')    # What is passed in the url. eg : /blogs/1
    return get_object_or_404(Blog, id=id_)

  def get_success_url(self):
    return reverse('blogs:blogs_list')




  