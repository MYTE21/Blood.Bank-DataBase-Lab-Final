from django import forms
from bloodapp.models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"