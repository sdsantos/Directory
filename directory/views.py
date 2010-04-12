# Create your views here.
from directory.models import *
from directory.utils import *

def index(request):
    companies = Company.objects.order_by('?')
    return render(request,'index.html',{'companies':companies})
    