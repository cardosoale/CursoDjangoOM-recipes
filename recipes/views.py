from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Alexandre',
    })


def recipes(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Alexandre',
    })
