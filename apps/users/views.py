# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from models import *
from django.contrib import messages
def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, "users/index.html", context)
def new(request):
    return render(request, "users/new.html")
def edit(request, id):
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "users/edit.html", context)
def show(request, id):
    print id
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "users/show.html", context)
def create(request):
    errors = User.objects.validator(request.POST, "create")
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/users/new")
    else:
        newuser = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        return redirect("/users/"+str(newuser.id))
def destroy(request, id):
    User.objects.get(id=int(id)).delete()
    return redirect("/users")
def update(request, id):
    errors = User.objects.validator(request.POST, "update")
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/users/new")
    else:
        User.objects.filter(id=int(id)).update(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        return redirect("/users/"+id)
