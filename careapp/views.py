from unicodedata import category
from django.shortcuts import render
from careapp.models import*

# Create your views here.
def home(request):
    #fetch all category
    cats=Category.objects.all()
    #fatch all  image
    images=Product.objects.all()
    data={'images':images,'cats':cats}
    return render(request,'home.html',data)

def show_category_page(request,cid):
    print(cid)
    #fatch all category
    cats=Category.objects.all()

    category=Category.objects.get(pk=cid)
    print(category)
     
    #fetch all selected category image
    images=Product.objects.filter(cat=category)
    data={'images':images,'cats':cats}
    return render(request,'home.html',data)