from django.shortcuts import render

# Create your views here.

def liste_articles(request):
    return render(request, 'liste_articles.html')