from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    # Return all the user objects and stores to data variable
    data=User.objects.all()
    context={"data":data}

    return render(request, "index.html", context)


def insertData(request):
    # Return all the user objects and stores to data variable
    data=User.objects.all()
    context={"data":data}

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

        # Display message for insertion
        messages.info(request,"Data Inserted Successfully")

        # redirect to index.html page
        return redirect("/")

    # render index.html page
    return render(request, "index.html", context)


def updateData(request,id):
    # Filter the user object and stores to d variable
    d=User.objects.get(id=id)
    context={"d":d}

    # if form is submitted then action request is handled
    if request.method=="POST":
        # gets & stores the form data to variables
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        address=request.POST['address']
        gender=request.POST['gender']

        # Filter the record by id
        edit=User.objects.get(id=id)

        # Update the details of that record
        edit.name=name
        edit.email=email
        edit.contact=contact
        edit.address=address
        edit.gender=gender

        # Save the updated record
        edit.save()

        # Display message for updation
        messages.warning(request,"Data Updated Successfully")

        # Once record is updated then it is redirected to index.html page
        return redirect("/")

    # render & redirect to edit.html page
    return render(request, "edit.html", context)


def deleteData(request,id):
    # Filter the user object and stores to d variable
    d=User.objects.get(id=id)
    
    # Delete the user record
    d.delete()

    # Display message for deletion
    messages.error(request,"Data Deleted Successfully")

    # Once record is deleted then it is redirected to index.html page
    return redirect("/")