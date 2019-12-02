from django.shortcuts import render

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from app.models import tblregister
from app.models import product,storage,processor
from app.models import powersupply,motherboard,monitor
from app.models import memory,laptop,headphone
from app.models import graphicscard,coolingsystem,cabinetcase

# Create your views here.


def sa(request):
    return render(request,'index.html')
def index(request):
    return render(request,'index.html')
def single(request):
    return render(request,'single.html')
def cooler(request):
    return render(request,'cooler.html')
def signup(request):
    return render(request,'signup.html')
def save(request):
    if request.method == 'POST':
        tc=tblregister()
        tc.name = request.POST.get('name')
        tc.gender = request.POST.get('gender')
        tc.dob = request.POST.get('dob')
        tc.email = request.POST.get('email')
        tc.uname = request.POST.get('uname')
        tc.password = request.POST.get('password')
        tc.save()
        return render(request,'login.html')
def login(request):
    return render(request,'login.html')
def log(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        pswd=request.POST.get('password')
        dt=tblregister.objects.all()
        flag=0
        for x in dt:
            if x.uname==user and x.password==pswd:
                flag=1
                return render(request,'mypage.html')
        if flag==0:
            return HttpResponse("invalid user name of or password")
def logout(request):
    try:
        del request.session['userid']
    except KeyError:
        pass
    return render(request,'index.html')
def mypage(request):
    return render(request,'mypage.html')
def add(request):
    return render(request,'addproduct.html')
def addpro(request):
    if request.method == "POST":
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save (photo.name,photo)
        upload_file_url = fs.url(filename)
        name = request.POST.get('name')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        brandname = request.POST.get('brandname')
        price = request.POST.get('price')
        image = upload_file_url
        if category == 'CabinetCase':
            tc = cabinetcase()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'CoolingSystem':
            tc = coolingsystem()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'GraphicsCard':
            tc = graphicscard()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Headphone':
            tc = headphone()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Laptop':
            tc = laptop()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Memory':
            tc = memory()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Monitor':
            tc = monitor()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Motherboard':
            tc = motherboard()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'PowerSupply':
            tc = powersupply()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Processor':
            tc = processor()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()
        if category == 'Storage':
            tc = storage()
            tc.name = name
            tc.category = category
            tc.subcategory = subcategory
            tc.brandname = brandname
            tc.price = price
            tc.image = image
            tc.save()

        return render(request,'addproduct.html')
    else:
        return HttpResponse("invalid data type")
def lap(request):
    lap = laptop.objects.all()
    return render(request,'laptop.html',{'Lap':lap})
def cabinet(request):
    cab = cabinetcase.objects.all()
    return render(request,'cabinet.html',{'Cab':cab})
def cooling(request):
    cool = coolingsystem.objects.all()
    return render(request,'coolingsystem.html',{'Cool':cool})
def graphics(request):
    cgraphics = graphicscard.objects.all()
    return render(request,'graphicscard.html',{'CGraphics':cgraphics})
def cheadphone(request):
    cchead = headphone.objects.all()
    return render(request,'headphone.html',{'CHead':cchead})
def cmemory(request):
    ccmemory = memory.objects.all()
    return render(request,'memory.html',{'CMemory':ccmemory})
def cmonitor(request):
    ccmonitor = monitor.objects.all()
    return render(request,'monitor.html',{'CMonitor':ccmonitor})
def mboard(request):
    board = motherboard.objects.all()
    return render(request,'motherboard.html',{'Board':board})
def power(request):
    power = powersupply.objects.all()
    return render(request,'power.html',{'Power':power})
def processing(request):
    process = processor.objects.all()
    return render(request,'processor.html',{'Process':process})
def storing(request):
    store = storage.objects.all()
    return render(request,'storage.html',{'Store':store})
def allproject(request):
    cool = coolingsystem.objects.all()
    return render(request,'allpro.html',{'Cool':cool})
def cs(request,id):
    data = coolingsystem.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def cab(request,id):
    data = cabinetcase.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def gc(request,id):
    data = graphicscard.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def hp(request,id):
    data = headphone.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def lp(request,id):
    data = laptop.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def my(request,id):
    data = memory.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def mr(request,id):
    data = monitor.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def mb(request,id):
    data = motherboard.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def ps(request,id):
    data = powersupply.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def pr(request,id):
    data = processor.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})
def sr(request,id):
    data = storage.objects.get(id=id)
    return render(request,'viewpage.html',{'Data':data})