from django.shortcuts import render

# Create your views here.
def home_view(request, ):
    return render(request, 'website/home.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')

