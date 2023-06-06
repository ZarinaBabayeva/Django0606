from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app.forms import ProductForm
# Create your views here.
def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    context = {
        'form': form,
    }   
    return render(request, 'pages/create.html', context)