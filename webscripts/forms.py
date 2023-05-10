from django import forms
from django.forms import ModelForm, Textarea, Select, HiddenInput
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as _
# from .input_validation_definitions import SCHOOL_YEAR_CHOICES
import datetime

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField(label="Αρχείο παρακολούθησης ύλης Γενικών Λυκείων από το MySchool.")