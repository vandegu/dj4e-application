from django.shortcuts import render

# Create your views here.

def index(request):
    # Index page of /home application

    # Context variable for sending info over to the template
    context = {}

    # Render the page by making a request for the html template
    return render(request,"index.html",context=context)
