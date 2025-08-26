from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.conf import settings
from datetime import datetime
# Create your views here.

class RestaurantSerializerView(APIView):
    def get(self,request):
        restaurant=Restaurant.objects.first()
        serializer=RestaurantSerializer(restaurant)
        return Response(serializer.data)

def contact_us(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form=ContactForm()
    return render(request,'home/contact_us.html',{'form':form})

def home_view(request):
    restaurant_name=settings.RESTAURANT_NAME
    restaurant_phone_number=settings.RESTAURANT_PHONE_NUMBER
    current_year = datetime.now().year
    return render(request,'home/home.html',{'restaurant_name':restaurant_name,'phone_number':restaurant_phone_number,'year':current_year})

def about_us(request):
    return render(request,'about_us.html')

def home(request):
    phone_number=settings.RESTAURANT_PHONE_NUMBER
    return render(request,'home/homepage.html',{'phone_number':phone_number})
