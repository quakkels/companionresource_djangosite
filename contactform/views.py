from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactFormForm
from .models import ContactForm

def contactform(request):
    form = ContactFormForm()
    context = { "form" : form }

    if request.method != "POST":
        return render(request, "contactform.html", context)
    
    form = ContactFormForm(data=request.POST)

    if not form.is_valid():
        context["form"] = form
        return render(request, "contactform.html", context)
    
    form.save()
    return redirect("/")
