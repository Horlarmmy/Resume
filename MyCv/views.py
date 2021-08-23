from django.shortcuts import render
from .forms import Contact
# Create your views here.
def index(request):
	form_class = Contact
	return render(request, 'index.html', {'form': form_class,})
