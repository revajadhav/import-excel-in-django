from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import temperature

# Create your views here.
 
def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        dbframe = pd.read_excel(filename)        
        for dbframe in dbframe.itertuples():
            obj = temperature.objects.create(year=dbframe.year,jan=dbframe.jan,feb=dbframe.feb,mar=dbframe.mar,
                                            apr=dbframe.apr,may=dbframe.may,jun=dbframe.jun,jul=dbframe.jul,
                                            aug=dbframe.aug,sep=dbframe.sep,oct=dbframe.oct,nov=dbframe.nov,
                                            dec=dbframe.dec,win=dbframe.win,spr=dbframe.spr,sum=dbframe.sum,
                                            aut=dbframe.aut,ann=dbframe.ann )  
                 
            obj.save()
            query_res = temperature.objects.all()
        return render(request, 'home.html', {
            'query_res': query_res
        })   
    return render(request, 'home.html')



