from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact_form(request):
   form = ContactForm()
   return render(request, 'index.html', {'form': form})

