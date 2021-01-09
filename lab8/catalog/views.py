from django.shortcuts import render

def index(request):
  return render(
        request,
        'index.html',
    )

def russia(request):
  return render(
        request,
        'russia.html',
    )

def greece(request):
  return render(
        request,
        'greece.html',
    )

def scandinavia(request):
  return render(
        request,
        'scandinavia.html',
    )

def china(request):
  return render(
        request,
        'china.html',
    )
