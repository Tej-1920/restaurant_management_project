from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Restaurant
from .serializers import RestaurantSerializer
from django.conf import settings
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
    return render(request,'home/home.html',{'restaurant_name':restaurant_name})
