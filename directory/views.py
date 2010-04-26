# Create your views here.
from directory.models import *
from directory.utils import *
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    companies = Company.objects.order_by('?')
    return render(request,'index.html',{'companies':companies})
    
def submit(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
           newCompany = form.save()
           return HttpResponseRedirect(reverse('index'))
    else:
        form = CompanyForm()
    
    return render(request,'submit.html',{'form':form})