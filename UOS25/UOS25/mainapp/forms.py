from django.forms import ModelForm
from mainapp.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'information']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['userId']
    