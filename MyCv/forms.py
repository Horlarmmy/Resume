from django import forms

class Contact(forms.Form):
	name = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	content = forms.CharField(required = True, widget= forms.Textarea)