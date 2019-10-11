from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('remove/<int:pack_id>', views.remove, name='remove'),
    path('add/<int:pack_id>', views.add, name='add'),
    path('adjust/<int:pack_id>/<str:change>', views.adjust, name='adjust'),
    path('', views.detail, name='detail')
]
