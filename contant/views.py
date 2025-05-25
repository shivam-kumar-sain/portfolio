from django.shortcuts import render, redirect
# Create your views here.
def view_home(request):
    return render(request,'home.html')

