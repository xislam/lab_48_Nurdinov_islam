
from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request, *args, **kwargs):

    product = Product.objects.all()
    return render(request, 'index.html', context={
        'product': product
    })


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'task.html', context={'product': product})


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
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category']

            )

            return redirect('task_view', pk=product.pk)

        else:

            return render(request, 'create.html', context={'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(data=request.POST)

    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'amount': product.amount,
            'category': product.category,
            'price': product.price
        })
        return render(request, 'update.html', context={'product': product, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.description = form.cleaned_data['description']
            product.name = form.cleaned_data['name']
            product.category = form.cleaned_data['category']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('task_view', pk=product.pk)


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')

