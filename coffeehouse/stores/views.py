from django.shortcuts import render

# Create your views here.
def detail(request, store_id=1):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    STORE_NAME = 'Downtown'
    store_address = {'street': 'Main #385', 'city': 'San Diego', 'state': 'CA'}
    store_amenities = ['WiFI', 'A/C']
    store_menu = ((0, ''), (1, 'Drinks'), (2, 'Food'))
    values_for_template = {'store_name': STORE_NAME, 'store_address': store_address, 'store_amenities': store_amenities, 'store_menu': store_menu}
    return render(request, 'stores/detail.html', values_for_template)

def detail(request, store_id=1, location='Moscow'):
    STORE_NAME = 'Downtown'
    store_address = {'street': 'Main #385', 'city': 'San Diego', 'state': 'CA'}
    store_amenities = ['WiFI', 'A/C']
    store_menu = ((0, ''), (1, 'Drinks'), (2, 'Food'))
    values_for_template = {'store_name': STORE_NAME, 'store_address': store_address, 'store_amenities': store_amenities, 'store_menu': store_menu}
    return render(request, 'stores/detail.html', values_for_template)

def index(request):
    return render(request, 'stores/index.html')
