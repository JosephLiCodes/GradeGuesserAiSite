from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length = 200)
    check = forms.BooleanField(required = False)

class UploadFileForm(forms.Form):
    title = forms.CharField(label = "input file", max_length=50)
    file = forms.FileField()
