from django.urls import path
from django.conf.urls import include
from . import views

# Arguments of path function: a URL pattern, a view function that will be called if the URL pattern is
# detected (this one comes from the function index() in the views.py file), and a name that we can use in
# href statements.
# Additionally, the use of <something> in the url pattern will capture the input url in that place and save
# it to the variable 'something'. In this case, the int:pk will capture an integer named 'pk' (as a book id).
# you can use more complex pattern matching with regex, by using the re_path() method instead of the path() one
# There is more info about this at https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views.

urlpatterns = [
    path('', views.index, name='index')
]
