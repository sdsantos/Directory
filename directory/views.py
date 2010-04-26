# Create your views here.
from directory.models import *
from directory.utils import *
from models import *
from forms import *
from django.http import HttpResponseRedirect

def index(request):
    companies = Company.objects.filter(approved='True').order_by('?')
    
    return render(request,'index.html',{'companies':companies})
    
def submit(request):
    if request.method == 'POST':
	form = CompanyForm(request.POST)
	
	if(form.is_valid()):
	    newCompany = form.save()
	    return HttpResponseRedirect('/../')
    else:
	form = CompanyForm()
    
    return render(request,'submit.html',{'form':form})