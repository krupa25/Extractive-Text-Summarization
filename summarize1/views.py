from django.shortcuts import render,redirect
from .models import Article
from summarize1.abstractive import Abstractive

# Create your views here.
def home(request):
    return render(request, "home.html")

def create(request):
    if request.method=="POST":
        art = Article()
        print("data============")
        article = request.POST.get("articles")
        print(request.POST.get("articles"))
        art.article =request.POST.get("articles")
        summary=Abstractive()
        out = summary.summarize(request.POST.get("articles"))
        print(out)
        art.summary = out
        art.save()
    return render(request, "home.html", {"summary":out,"articles": article})

def output(request):
    return redirect("/front")

