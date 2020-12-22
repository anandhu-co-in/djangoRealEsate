from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def index(request):
    return render(request,'listings/listings.html')

def listing(request,listing_id):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')
