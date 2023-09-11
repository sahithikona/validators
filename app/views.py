from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse



# Create your views here.
def insert_student(request):
    sfeo=Studentform()
    d={"sfeo":sfeo}
    if request.method=="POST":
        sfdo=Studentform(request.POST)
        if sfdo.is_valid():
            return HttpResponse(str(sfdo.cleaned_data))
        else:
            return HttpResponse("invalid data")

    return render(request,"insert_student.html",d)



