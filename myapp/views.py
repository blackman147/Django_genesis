from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.forms import CohortForm, NativeForm, ThoughtForm
from .models import Native


def home(request):
    return render(request, "home.html")


def display(request):
    native = Native.objects.all()
    print(native)
    context = {
        "native": native
    }
    return render(request, "display.html", context)


def cohort_form(request):
    if request.method == "POST":
        cohort = CohortForm(request.POST)
        if cohort.is_valid():
            cohort.save()
            return redirect('cohort')

    context = {
        "form": CohortForm
    }
    return render(request, "cohort.html", context)


def native_form(request):
    if request.method == "POST":
        native = NativeForm(request.POST, request.FILES)
        if native.is_valid():
            native.save()
            return redirect('native')

    context = {
        "form": NativeForm
    }

    return render(request, "native.html", context)


def thought_form(request):
    if request.method == "POST":
        thought = CohortForm(request.POST)
        if thought.is_valid():
            thought.save()
            return redirect('thought')

    context = {
        "form": ThoughtForm
    }
    return render(request, "thought.html", context)
