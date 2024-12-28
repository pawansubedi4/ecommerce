from django.shortcuts import render,redirect
from .models import productsnew,commentbox
# from django.contrib.auth.models import comments
# from django.views.generic import CreateView

# Create your views here.
def index(request):
    data={
        'productdata':productsnew.objects.all()
    }
    return render(request, 'index.html',data)

def category(request):
    return render(request, 'category.html')

def about(request):
    return render(request, 'about.html')

def rasan(request):
    data={
        'productdata':productsnew.objects.all()
    }
    data1=data['productdata'][category]
    return render(request, 'rasan.html',data,data1) 

def book(request):
    data={
        'productdata':productsnew.objects.all()
    }
    return render(request, 'book.html',data)

def vehicle(request):
    data={
        'productdata':productsnew.objects.all()
    }
    return render(request, 'vehicles.html',data)

def mobile(request):
    data={
        'productdata':productsnew.objects.all()
    }

    return render(request, 'mobile.html',data)

def beauty(request):
    data={
        'productdata':productsnew.objects.all()
    }

    return render(request, 'beauty.html',data)

# class commentsCreateView(CreateView):
#     model=comments
#     template_name='contact.html'
#     fields=['name','email1','phone_number1','comments1']

def contact(request):
        if request.method=="post":
            name =request.post.get('Name')
            email =request.post.get('Email')
            phone =request.post.get('Phone')
            com =request.post.get('Comments')
            commentbox.objects.create(name=name,email=email,phone_number=phone,comments=com)
    
            return redirect('index')
        else:
            return render(request,'contact.html')

def buy(requests,id):
    if requests.method=="post":
        pass
    else:
        data123={
            'product':productsnew.objects.get(id=id)
        }
        return render(requests,'buy.html',data123)







