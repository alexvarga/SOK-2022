from django import forms


class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': 'text/html'}))

