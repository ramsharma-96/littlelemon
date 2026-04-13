from urllib import request

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import MenuItem, Booking
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics
from rest_framework import viewsets

def sayHello(request):
 return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer