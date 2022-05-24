from django.contrib import admin
from django.urls import path
# import views file from app folder: [mainApp]
from mainApp import views

# django admin header customization
# text
admin.site.site_header = "Admin Section Header"
admin.site.site_title = "Title"
admin.site.index_title = "Index Page Title"

urlpatterns = [
# set homepage
    path('', views.index, name="home"),
# change [pageName] with your page name
# url address path name: [pathName]
# function name defined in views.py: [viewsFunctionName]
# page name: [pageName]
#	path('pathName', views.viewsFunctionName, name="pageName" ),
# --> add address below
# # page:
#	path('pathName', views.viewsFunctionName, name="pageName" ),
# form page:
	path('form', views.form, name="form" ),
]