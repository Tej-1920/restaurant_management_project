from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.

def homepage(request):
    restaurent=
def contact_us(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form=ContactForm()
    return render(request,'home/contact_us.html',{'form':form})
