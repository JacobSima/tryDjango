from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm


# Convert this to class base view
def home(request, *args, **kwargs):
  return render(request,'courses.html',{})


class CourseObjectMixing(object):
  model = Course
  loopup = 'id'

  def get_object(self):
    loopup = self.kwargs.get(self.loopup)
    obj = None
    if loopup is not None:
      obj = get_object_or_404(Course, id =loopup)
    return obj


# Base VIEW class = VIEW
class CourseView(View):
  template_name_with_id = 'course_detail.html'
  template_name_No_id = 'courses.html'
  queryset = Course.objects.all()

  def get_queryset(self):
    return self.queryset

  def get (self,request, id=None, *args, **kwargs):           # The name of the function depends on the HTTP methds initiate , id=None: is not required
    context = {}
    if id is not None:
      obj = get_object_or_404(Course, id=id)
      context['object'] = obj
      return render(request,self.template_name_with_id,context)
    else:
      context = {'object_list':self.get_queryset()}
      return render(request, self.template_name_No_id,context)




# To Create something you need the post and get methods
class CourseCreateView(View):
  template_name = 'delete.html'

  def get(self,request, *args, **kwargs):
    form = CourseModelForm()
    context = {'form':form}
    return render(request, self.template_name,context)

  def post(self,request, *args, **kwargs):
    form = CourseModelForm(request.POST)
    context = {'form':form}
    if form.is_valid():
      form.save()
    return render(request, self.template_name,context)







class CourseUpdateView(CourseObjectMixing,View):
  template_name = 'update.html'

  def get(self,request,id=None, *args, **kwargs):
    context = {}
    obj = self.get_object()
    if obj is not None:
      form = CourseModelForm(instance=obj)
      context['object'] = obj
      context['form'] = form
    return render(request, self.template_name,context)

  def post(self,request,id=None, *args, **kwargs):
    context = {}
    obj = self.get_object()
    print(obj)
    if obj is not None:
      form = CourseModelForm(request.POST,instance=obj)
      if form.is_valid():
        form.save()
        context['object'] = obj
        context['form'] = form
    return render(request, self.template_name,context)




class CourseDeleteView(View):
  template_name = 'delete.html'

  def get_object(self):
      id = self.kwargs.get('id')
      obj = None
      if id is not None:
        obj = get_object_or_404(Course, id =id)
      return obj

  def get(self,request,id=None, *args, **kwargs):
    context = {}
    obj = self.get_object()
    if obj is not None:
      form = CourseModelForm(instance=obj)
      context['object'] = obj
    return render(request, self.template_name,context)

  def post(self,request,id=None, *args, **kwargs):
    context = {}
    obj = self.get_object()
    if obj is not None:
      obj.delete()
      context['object'] = None
      return redirect('/courses/')
    return render(request, self.template_name,context)


















  














