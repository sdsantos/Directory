# Create your views here.
from directory.models import *
from directory.utils import *
from models import *
from forms import *
from django.http import HttpResponseRedirect

def index(request):
    companies = Company.objects.order_by('?')
    return render(request,'index.html',{'companies':companies})
    
def submit(request):
    if request.method == 'POST':
	form = CompanyForm(request.POST)
	
	if(form.is_valid()):
	    newCompany = Company(
		name = form.cleaned_data['name'],
		logo = form.cleaned_data['logo'],
		description = form.cleaned_data['description'],
		website = form.cleaned_data['website'],
		email = form.cleaned_data['email'],
		address = form.cleaned_data['address'],
		phone = form.cleaned_data['phone'],
		year = form.cleaned_data['year'],
		map_lat = form.cleaned_data['map_lat'],
		map_lon = form.cleaned_data['map_lon'],
		tags = form.cleaned_data['tags'],	    
	    )
	    newCompany.save()
    
	    return HttpResponseRedirect('/../')
    else:
	form = CompanyForm()
    
    return render(request,'submit.html',{'form':form})