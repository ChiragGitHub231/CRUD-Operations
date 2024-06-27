from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        print(name, email, contact, address, gender)

    return render(request, "index.html")