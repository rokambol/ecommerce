from django.shortcuts import render

def index(requiest):
    """ A view that display index page """
    return render(requiest, "index.html")
