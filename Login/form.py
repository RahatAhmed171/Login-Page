from django import forms
class Geeksform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)