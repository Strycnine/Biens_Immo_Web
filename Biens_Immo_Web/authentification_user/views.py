from django.shortcuts import render

# Create your views here.
def auth(request):
    title = ('Login')
    return render(request, 'login.html', {"title":title})
