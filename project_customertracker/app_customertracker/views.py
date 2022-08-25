from django.shortcuts import render

from app_customertracker.forms import ProductCreateForm

# Create your views here.
def product_index(request):
    template = 'products/index.html'
    context = {
        "data": {
            "first_name": "Maila",
            "last_name": "Byakul",
            "email": "byakul@gmail.com"
        }
    }
    return render(request, template, context)
    
def product_create(request):
    create_form = ProductCreateForm
    context = {"form": create_form}
    template = 'products/create.html'
    return render(request, template, context)
