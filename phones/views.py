from django.shortcuts import render

from .models import Phone


def index(request):
    phone_list = Phone.objects.all()
    context = {
        'phone_list': phone_list,
    }
    return render(request, 'phones/index.html', context)
