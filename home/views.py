from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.conf import settings
from products.models import Products
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def index(request):
    products = Products.objects.filter(is_active=True, is_brand=True)
    category_name = 'Features Items'
    title = 'Index'
    return render(request, 'home/index.html', locals())

def faq(request):
    title = 'Faq'
    return render(request, 'home/faq.html', locals())

def testimonials(request):
    title = 'Testimonials'
    return render(request, 'home/testimonials.html', locals())

def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid:
            #name = form.cleaned_data['name']
            subject = form['subject']
            message = form['message']
            sender = form['email']
            try:
                send_mail(subject, message, sender, list(settings.CONTACT_EMAIL))
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('home/contact-us.html', {'form': form})
    title = 'Contact US'
    return render(request, 'home/contact-us.html', {'form': form, 'title': title})

