from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ProductImage, Order
from django.template import loader
from .forms import ProductForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    product_list = Product.objects.all()
   
    context = {
        'product_list':product_list,

    }
    return render(request,'watch/index.html',context)
class IndexClassView(ListView):
    model = Product;
    template_name = 'watch/index.html' 
    context_object_name = 'product_list'   


def product(request):
    return HttpResponse('<h1>This is product views</h1>')

def detail(request,product_id):
    product = Product.objects.get(pk = product_id)
    context = {
        'product': product,
    }
    return render(request,'watch/detail.html',context)
class WatchDetail(DetailView):
    model = Product
    template_name = 'watch/detail.html'  
      
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('watch:index')
        
    return render(request, 'watch/product-form.html', {'form': form})   
# this is a class based view for create product  
class CreateProduct(CreateView):
        model = Product
        fields = ['product_name','product_category','product_desc','product_model', 'product_price','product_image']
        template_name = 'watch/product-form.html'
        def form_valid(self,form):
            form.instance.user_name = self.request.user
            return super().form_valid(form)

  

def update_product(request,id):
    product = Product.objects.get(id = id)            
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('watch:index')

    return render(request, 'watch/product-form.html', {'form': form, 'product': product}) 

def remove_product(request,id):
    product = Product.objects.get(id = id)  

    if request.method == 'POST':
        product.remove()
        return redirect('watch:index')

    return render(request, 'watch/product-remove.html', {'product':product})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total) 
        order.save()  

    return render(request,'watch/checkout.html')



def home(request):
    product = Product.objects.all
    context = {
        'product': product,
    }
    return render(request,'watch/home.html',context)      