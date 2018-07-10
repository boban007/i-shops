from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact-us/', views.contact_us, name='contact_us')
]