from django import forms

choices = [
    ("entertain","Entertainment"),
    ("edu","Education"),
    ("politics","Politics"),
    ("food","Food"),
    ("medical","Medical"),
    ("photo","Photography"),
    ("news","News"),
    ("environ","Evvironment"),
    ("travel","Travel"),
    ("kids","Kids"),
    ("other","Other")
]

class Addblog(forms.Form):
    title = forms.CharField(max_length=100)
    post = forms.CharField(widget=forms.Textarea)
    categories = forms.CharField(widget=forms.Select(choices=choices))