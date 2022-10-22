from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpRequest
from django.db.models import Q, Count, Avg
from .models import Rating
from .form import Rateform, Captcha
from .models import Contact
from .form import Contactform
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'main/home.html', {'page':1})

def contact_page(request):
    allrate=0
    reviews = Rating.objects.aggregate(count=Count('rating'))
    if reviews['count'] is not None:
        allrate=int(reviews['count'])
    
    avg=0
    reviews = Rating.objects.aggregate(average=Avg('rating'))
    if reviews['average'] is not None:
        avg = round(float(reviews['average']),1)
    rate=Rating.objects.order_by('-date')[:5]

    cform=Captcha()
    rform=Captcha()

    if request.method == 'POST':
        captcha=Captcha(request.POST)
        form1 = Rateform(request.POST)
        form2 = Contactform(request.POST)
        if captcha.is_valid():
            if form1.is_valid():
                form1.save()
                messages.success(request,'Köszönjük az értékelésedet!')
            elif form2.is_valid():
                form2.save()
                messages.success(request,'Köszönjük az üzenetedet!')
        else:
            messages.error(request,'A Captcha hibás!')
            return redirect(contact_page)
        return redirect(contact_page)


    return render(request, 'main/contact.html', {'rate':rate, 'allrate':allrate, 'avg':avg, 'page':3, 'cform': cform, 'rform': rform})


def about_page(request):
    return render(request, 'main/about.html', {'page':2})
