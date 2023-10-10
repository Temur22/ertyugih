from django import forms


class NewForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()


