from django.contrib import admin
from django.urls import path
from list.views import buy_list, add_item
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', buy_list, name='buy_list'),
    path('add/', add_item, name='add_item')
]
