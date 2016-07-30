from django.shortcuts import render
from django.http import HttpResponse, Http404
from sunlight import openstates
from django.utils import http

# page where user can search for bills
def index(request):
    return render(request, 'billtrack/form.html')

# list all the bills from a certain state
def search(request):
    if request.method == 'POST':
        state = request.POST.get('state', None)
        keyword = request.POST.get('keyword', None)
        # call sunlightfoundation api here
        bills = openstates.bills(state=state, q=keyword)
        print(len(bills))
        context = {'bills': bills, 'state': state, 'keyword': keyword}
        return render(request, 'billtrack/bills.html', context)
    else:
        return render(request, 'billtrack/form.html')

def detail(request, state, session, bill_id):
    bill = openstates.bill_detail(state=state, session=session, bill_id=bill_id)
    print(bill)
    return render(request, 'billtrack/detail.html', {'bill': bill})
