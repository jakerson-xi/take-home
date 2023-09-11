from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Purchase
from django.core import serializers
from .forms import PurchaseForm
import sweetify
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Welcome")
# Create your views here.


#view the lists of Purchase data
def viewList(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Purchase Saved', text='Purchase data has been added.', persistent='Done')
            return redirect('/viewList')
           
    form = PurchaseForm
    #retrieve all the data from Purchase model
    purchases = Purchase.objects.all().order_by('-timestamp')
    return render(request,'PurchasesList.html', {'purchases':purchases, 'form':form})

# delete purchase data with the or_number
def delete_purchase(request, or_numbers):

    purchase = Purchase.objects.get(or_number = or_numbers)
    sweetify.success(request, 'Purchase data deleted', text='Purchase data (OR # ' + or_numbers + ') has been deleted.', persistent='Done')
    purchase.delete()
    return redirect('/viewList')

# update purchase data with the or_number
def update_purchase(request, or_numbers):
    purchase = Purchase.objects.get(or_number = or_numbers)
    form = PurchaseForm(request.POST or None, instance=purchase)
    if form.is_valid():
        form.instance.timestamp = purchase.timestamp
        form.save()
        sweetify.success(request, 'Purchase data successfully updated', text='Purchase data (OR # ' + or_numbers + ') has been updated.', persistent='Done')
        return redirect('/viewList')
    return render(request,'editPurchase.html', {'purchase':purchase, 'form':form})

    

