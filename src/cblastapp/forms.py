from django import forms


from .models import EstRequest

class EstRequestForm(forms.ModelForm):
	class Meta:
		model = EstRequest