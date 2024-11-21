from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *


# Create your views here.
#fbv in a string
def fbv(request):
    return HttpResponse('<h1>fbv in a string</h1>')

#cbv in a string
class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>cbv in a string</h1>')
    
#fbv in a templateview
def fbvhtml(request):
    return render(request,'fbvhtml.html')

#cbv in a templateview
class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')
    
#fbv insert data
def fbvid(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Done')
        else:
            return HttpResponse('Invalid')
    return render(request,'fbvid.html',d)

#cbv insert data

class CbvInsert(View):
    def get(self,request):
        ESFO=StudentForm()
        d={'ESFO':ESFO}
        return render(request,'CbvInsert.html',d)
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('done')
        else:
            return HttpResponse('invalid')
