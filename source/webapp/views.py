from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import *
from webapp.models import Product


def index_view(request, *args, **kwargs):
    product = Product.objects.filter(category='active').order_by('-creation_date')
    form = SeacrhForm()
    return render(request, 'index.html', context={
        'product': product,
        'form': form
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def product_create_view(request, *args, **kwargs):
    if request.method == 'GET':

        form = ProductForm()

        return render(request, 'create.html', context={'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount']

            )

            return redirect('product_view', pk=product.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'price': product.price,
            'amount': product.amount

        })
        return render(request, 'update.html', context={'product': product, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.amount = form.cleaned_data['amount']
            product.save()
            return redirect('product_view', pk=product.pk)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')


def product_seach(request):
    name = request.GET.get('search')
    product = Product.objects.filter(name__contains=name).filter(category='active')
    return render(request, 'index.html', context={
        'product': product
    })
