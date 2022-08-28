from django.shortcuts import render

from app_customertracker.forms import ProductCreateForm

from .models import AppUser, Product

# Create your views here.
def product_index(request):
    template = 'products/index.html'
    app_users = AppUser.objects.all()
    context = {"app_users": app_users}
    return render(request, template, context)
    
def product_create(request):
    create_form = ProductCreateForm
    context = {"form": create_form}

    if request.method == "POST":
        # creating model object
        app_user = AppUser()

        # assigning value to attributes
        app_user.first_name = request.POST.get('first_name')
        app_user.middle_name = request.POST.get('middle_name')
        app_user.last_name = request.POST.get('last_name')
        app_user.email = request.POST.get('email')
        app_user.password = request.POST.get('password')

        # storing value to db
        app_user.save()
        
        context.setdefault("msg", "Successfully Added")
        template = 'products/create.html'
        return render(request, template, context)

    template = 'products/create.html'
    return render(request, template, context)
