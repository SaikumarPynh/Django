from django.shortcuts import render
from django.http import HttpResponse
from .models import Dynamic 
# Create your views here.
def index(request):
    dyn = Dynamic()
    dyn.no = 100
    dyn.name = "OfficialHotel"
    dyn.title  = " think before do"
    dyn.desc  = " the title says we need to think before anything done, before wasting time before not taking important decisions and when doing wrong things"
    dyn2 = Dynamic()
    dyn2.no = 300
    dyn2.name = "OfficialRestuarants"
    dyn2.title = " Best hotels to stay"
    return render(request, 'index.html',{'dyn' : dyn, 'dyn2': dyn2} )

