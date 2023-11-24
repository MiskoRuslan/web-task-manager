from django import forms
from django.contrib.auth.forms import UserCreationForm

from web_service.models import Worker, Task


class PositionForm(forms.Form):
    name = forms.CharField(max_length=255)


class TaskTypeForm(forms.Form):
    name = forms.CharField(max_length=255)


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("position", "first_name", "last_name", )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'assignees': forms.CheckboxSelectMultiple,
        }


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )
