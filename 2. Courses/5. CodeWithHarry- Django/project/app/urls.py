from django.contrib import admin
from django.urls import path
# import views file
from app import views

# url dispatching
urlpatterns = [
#	path('', .urls),
# set homepage
    path('', views.index, name="home"),
# change [pageName] with your page name
# about page
	path('about', views.about, name="about" ),
# # contact page
	path('contact', views.contact, name="contact" ),
# # pageName page
# #	path('pageName', views.pageName, name="pageName" ),
]
    