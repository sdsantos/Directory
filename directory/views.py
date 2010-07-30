# -*- coding: utf-8 -*-

# Create your views here.
from directory.models import *
from directory.utils import *
from models import *
from forms import *
from django.http import HttpResponseRedirect

def index(request):
    success = 'success' in request.GET and request.GET['success']
    
    if 'company' in request.GET:
        company_id = request.GET['company']
        try:
            Company.objects.get(id=company_id, approved=True)
        except:
            company_id = None
    else:
        company_id = None
            
    
    companies = Company.objects.filter(approved='True').order_by('?')
    return render(request,'index.html',{'companies':companies, 'success':success, 'company_id':company_id})
    
def submit(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        
        if form.is_valid():
            newCompany = form.save()
            return HttpResponseRedirect('/../?success=true')
    else:
        form = CompanyForm()
    
    return render(request,'submit.html',{'form':form})