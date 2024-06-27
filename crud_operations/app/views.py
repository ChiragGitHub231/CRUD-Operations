from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    # Return all the user objects and stores to data variable
    data=User.objects.all()
    context={"data":data}

    return render(request, "index.html", context)

def insertData(request):
    # if form is submitted then action request is handled
    if request.method=="POST":
        # gets & stores the form data to variables
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        # Create an instance of User Model with form data and save the data
        query=User(name=name, email=email, contact=contact, address=address, gender=gender)
        query.save()

    # render & redirect to index.html page
    return render(request, "index.html")