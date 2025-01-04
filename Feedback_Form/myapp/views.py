from django.shortcuts import render,redirect
from myapp import form
from myapp.form import Feedback_Form1
from myapp.models import Feedback_Form

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Feedback_Form1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            form = Feedback_Form1()

    form =Feedback_Form1()   
    return render(request,'index.html',{'form':form})

def thanks(request):
    return render(request,'thanks.html')

def getfb(request):
    fb = Feedback_Form.objects.all()
    return render(request,'getfeedback.html',{'feedbacks':fb}) 