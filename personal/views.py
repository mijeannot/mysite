from django.shortcuts import render
from personal.models import Question

# Create your views here.
def home(request):
    context = {}
    context["questions"] = Question.objects.all()
    return render(request, "personal/home.html", context)


def about(request):
    return render(request, "personal/about.html", {"aboutpage": "about page"})


def contact(request):
    return render(request, "personal/contact.html", {"contactpage": "contact us"})
