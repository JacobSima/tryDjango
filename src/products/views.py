from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm,RawProductForm
from django.http import Http404



def product_list_view(request):
  queryset = Product.objects.all()
  context ={
    'object_list':queryset
  }
  return render(request,'products/product_list.html',context)


def dynamic_lookup_view(request,my_id):
  # obj = Product.objects.get(id=my_id)
  # obj = get_object_or_404(Product,id=my_id)
  try:  
    obj = Product.objects.get(id=my_id)
  except Product.DoesNotExist:
    raise Http404
  context = {
   'object':obj
  }
  return render(request,"products/dynamic_lookup.html",context)


def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ProductForm # re-render this form to clear the fields
  context = {
   'form':form
  }
  return render(request,'products/product_create.html',context)



# def product_create_view(request):
#   if request.method =="POST":
#     my_new_title = request.POST['title']
#     # Product.objects.create(title=my_new_title)
#     context = {}
#   return render(request,'products/product_create.html',context)




# def product_create_view(request):
#   my_form = RawProductForm()
#   if request.method == 'POST':
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       #now the data is good
#       #print(my_form.cleaned_data)   #{'title': 'uuj', 'description': 'ddidk', 'price': Decimal('122')}
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context = {'form':my_form}
#   return render(request,'products/product_create.html',context)




def product_delete_view(request,id):
  obj = get_object_or_404(Product, id=id)
  if request.method == "POST":
    #confirming delete
    obj.delete()
    return redirect('../../')
  return render(request,"products/product_delete.html",{'object':obj})



