from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def upload_csv(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        title = "Upload d'une nouvelle Data"
        return render(request, 'form.html', {"title":title})
    else:
        return redirect('/')
