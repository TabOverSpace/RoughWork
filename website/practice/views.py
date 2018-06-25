from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def algorithms(request):
    return render(request, 'practice/algorithms.html', {})

def data_structures(request):
    return render(request, 'practice/data_structures.html', {})

def programming_languages(request):
    return render(request, 'practice/programming_languages.html', {})

def codemirror(request):
    return render(request, 'practice/codemirror.html', {})
