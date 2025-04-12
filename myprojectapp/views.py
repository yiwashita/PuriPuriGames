from django.shortcuts import render

# Create your views here.
#追加
def myprojectfunction(request):
    return render(request, 'index.html')