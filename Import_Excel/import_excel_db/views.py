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
        df1 = pd.read_excel(filename, sheet_name=('England_Tmax')) 
        df2= pd.read_excel(filename, sheet_name=('England_Tmin')) 
        df3= pd.read_excel(filename, sheet_name=('Scotland_Tmax')) 
        df4= pd.read_excel(filename, sheet_name=('Scotland_Tmin')) 
        empexceldata = pd.concat([df1, df2, df3, df4])

        dbframe= empexceldata   
        for dbframe in dbframe.itertuples():
            obj = temperature.objects.create(year=dbframe.year,jan=dbframe.jan,feb=dbframe.feb,mar=dbframe.mar,
                                            apr=dbframe.apr,may=dbframe.may,jun=dbframe.jun,jul=dbframe.jul,
                                            aug=dbframe.aug,sep=dbframe.sep,oct=dbframe.oct,nov=dbframe.nov,
                                            dec=dbframe.dec,win=dbframe.win,spr=dbframe.spr,sum=dbframe.sum,
                                            aut=dbframe.aut,ann=dbframe.ann )  
                 
            obj.save()
            query_res = temperature.objects.all()
        return render(request, 'result.html', {
            'query_res': query_res
        })   
    return render(request, 'home.html')



