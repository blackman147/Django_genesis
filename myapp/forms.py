from django import forms

from myapp.models import Cohort, Native


class CohortForm(forms.ModelForm):

    class Meta:
        model = Cohort
        fields = "__all__"


class NativeForm(forms.ModelForm):
    class Meta:
        model = Native
        fields = "__all__"

