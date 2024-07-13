from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
        ).filter(
            is_published=True,
            is_on_main=True,
            category__is_published=True
            )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
