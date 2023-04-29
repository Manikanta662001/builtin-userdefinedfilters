from django.shortcuts import render

# Create your views here.
def filters(request):
    data='hAi DJANgo and PYThoN'
    import datetime
    dt=datetime.date.today()
    d={'data':data,'dt':dt,'c':10}
    return render(request,'filters.html',d)
def userdefinedfilters(request):
    data='hAi DJANgo and PYThoN'
    d={'data':data}
    return render(request,'userdefinedfilters.html',d)




