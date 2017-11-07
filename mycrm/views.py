from django.shortcuts import render

# Create your views here.


def test_page(request):
    return render(request, 'test_test_page.html', {'a':23, 'b':[1,4,3,4,5,'napis','kartówka']})

def index_page(request):
    return render(request, 'index.html', {})

def user_page(request):
    return render(request, 'user.html', {})

def company_page(request):
    return render(request, 'company.html', {})