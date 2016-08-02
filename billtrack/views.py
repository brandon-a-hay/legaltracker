from django.shortcuts import render
from django.http import HttpResponse, Http404
from sunlight import openstates
from django.utils import http
import requests

# page where user can search for bills
def index(request):
    return render(request, 'billtrack/form.html')

# list all the bills from a certain state
def search(request):
    if request.method == 'POST':
        state = request.POST.get('state', None)
        keyword = request.POST.get('keyword', None)

        # call sunlightfoundation api for state legislation
        bills = openstates.bills(state=state, q=keyword)

        # call api for federal legislation data
        fed_bills_response = requests.get('https://www.govtrack.us/api/v2/bill?q=' + keyword)
        if fed_bills_response.status_code == 200:
            fed_bills = fed_bills_response.json()
        else:
            fed_bills = None

        context = {'bills': bills, 'fed_bills': fed_bills, 'state': state, 'keyword': keyword}
        return render(request, 'billtrack/bills.html', context)
    else:
        return render(request, 'billtrack/form.html')

def detail(request, state, session, bill_id):
    bill = openstates.bill_detail(state=state, session=session, bill_id=bill_id)
    print(bill)
    return render(request, 'billtrack/detail.html', {'bill': bill})

def fed_bill_detail(request, bill_id):
    bill_response = requests.get('https://www.govtrack.us/api/v2/bill/' + bill_id)
    if bill_response.status_code == 200:
        bill = bill_response.json()
        print(bill)
    else:
        bill = None
    return render(request, 'billtrack/fed_bill_detail.html', {'bill': bill})
