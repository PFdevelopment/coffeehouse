from django.shortcuts import render

# Create your views here.
def detail(request, store_id=1):
    # Access store_id with store_id variable
    return render(request, 'stores/detail.html')

def detail(request, store_id=1, location='Moscow'):
    return render(request, 'stores/detail.html')
