from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class FormActualizar(forms.Form):
    index = forms.CharField(max_length=50)
    file = forms.FileField()