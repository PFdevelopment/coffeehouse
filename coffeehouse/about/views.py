from django.shortcuts import render

# Create your views here.
def index(request):
    pass

def contact(request):
    # Contend of request or database extracted here
    # and passed to the template to display
    return render(request, 'about/contact.html')
