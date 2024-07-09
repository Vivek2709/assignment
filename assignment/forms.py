from django import forms

class EventForm(forms.Form):
    query = forms.CharField(label='Enter a historic event name', max_length=100)

class UserDataForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.TextInput(attrs={'type': 'date'}))