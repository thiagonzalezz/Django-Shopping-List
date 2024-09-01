from django.shortcuts import render, redirect
from .models import List

# Create your views here.
def buy_list(request):
        lists = List.objects.all()
        return render(request, 'buy_list.html', {
            'lists': lists
        })
def add_item(request):
    if request.method == 'POST':
        item = request.POST['item']
        list = List(item=item)
        list.save()
        return redirect('buy_list')
    else:
        return render(request, 'add_item.html')
        