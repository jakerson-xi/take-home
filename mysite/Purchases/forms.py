from django import forms 
from django.forms import ModelForm
from .models import Purchase

#Create a Purchase from
class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ('sold_to', 'description', 'or_number', 'total_amount', 'quantity', 'remarks')
        widgets = {
            'sold_to': forms.TextInput(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter customer\'s name:'}),
            'description': forms.TextInput(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter product\'s description:'}),
            'or_number':forms.TextInput(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter OR number:'}),
            'total_amount': forms.TextInput(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter total amount:'
                                              }),
            'quantity': forms.TextInput(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter quantity:',
                                              'type':'number'}),
            'remarks': forms.Textarea(attrs={'class':'form-control my-2',
                                              'placeholder': 'Enter remarks:',
                                              'rows':'3'}),
        }
        labels = {
             'sold_to': 'Sold to:',
            'description':'Description:' ,
            'or_number': 'OR number:',
            'total_amount': 'Total Amount:',
            'quantity': 'Quantity:',
            'remarks': 'Remarks:',
        }

