from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Restaurant
from .serializers import RestaurantSerializer

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
