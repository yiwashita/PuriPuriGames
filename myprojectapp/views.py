from django.shortcuts import render

# Create your views here.
#追加
def myprojectfunction(request):
    return render(request, 'index.html')

def recipe(request):
    return render(request, 'recipe.html')

def BrockDestroy(request):
    return render(request, 'BrockDestroy.html')

def unity_index(request):
    return render(request, 'unity_index.html')
