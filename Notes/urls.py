"""Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views
urlpatterns = [
	path('',views.register),
	path('admin/', admin.site.urls),
	path('createNote/<int:reqId>',views.createNote,name="create"),
	path('viewNote/<int:reqId>',views.viewNote,name="view"),
	path('deleteNote/<int:Id>',views.deleteNote,name="deleteNote"),
	path('update/<int:Id>',views.update,name="update"),
	path("register/", views.register, name="register"),
	path("login", views.login_req, name="login"),
	path('signout/',views.signout,name='signout'),
]

