from django.shortcuts import render
from mainApp import models

# Create your views here.
# homepage
def index(request):
    return render(request, 'index.html')
# method for pages
# pageName method
#   def method(request):
#       return render(request, ''pageName.html)
# --> add method below
# # page
# def PageViewMethod(request):
#   return render(request, 'staticPage.html')
# form page
def form(request):
  return render(request, 'form.html')