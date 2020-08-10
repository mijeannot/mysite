from django.shortcuts import render

# Create your views here.
def home(request):
    # adict = {"homepage": "home page"}
    # return render(request, "personal/home.html", adict)
    return render(request, "personal/home.html", {"homepage": "home page"})


def about(request):
    return render(request, "personal/about.html", {"aboutpage": "about page"})

