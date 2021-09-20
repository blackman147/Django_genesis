from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.forms import CohortForm, NativeForm


def login(self):
    return HttpResponse('this is my login page')


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
        native = NativeForm(request.POST)
        if native.is_valid():
            native.save()
            return redirect('native')

    context = {
        "form": NativeForm
    }

    return render(request, "native.html", context)
