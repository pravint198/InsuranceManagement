from django import forms
from customers.models import Customers,Policies
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class CustomerForm(forms.ModelForm):

	class Meta:
		model=Customers
		exclude=['username']
		widgets={
				'name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control','style':{'margin-bottom':'12px'}}),
				'father_name':forms.TextInput(attrs={'placeholder':'Father\'s Name','class':'form-control'}),
				'mother_name':forms.TextInput(attrs={'placeholder':'Mother\'s Name','class':'form-control'}),
				'spouse_name':forms.TextInput(attrs={'placeholder':'Spouse\'s Name','class':'form-control','readonly':'true'}),
				'gender':forms.Select(attrs={'class':'form-control'}),
				'is_married':forms.Select(attrs={'class':'form-control bottomMargin'}),
				'dob':forms.SelectDateWidget(attrs={'placeholder':'Date Of Birth'},years=range(1900,2100)),
				'place_of_birth':forms.TextInput(attrs={'placeholder':'Place of Birth','class':'form-control'}),
				'correspondence_address':forms.Textarea(attrs={'placeholder':'Correspondence Address','class':'form-control bottomMargin','rows':'4'}),
				'permanent_address':forms.Textarea(attrs={'placeholder':'Permanent Address','class':'form-control','rows':'4'}),
				'pan':forms.TextInput(attrs={'placeholder':'PAN Number','class':'form-control'}),
				'aadhar':forms.NumberInput(attrs={'placeholder':'Aadhar Number','class':'form-control'}),
				'education':forms.TextInput(attrs={'placeholder':'Education','class':'form-control'}),
				'mobile':forms.NumberInput(attrs={'placeholder':'Mobile','class':'form-control'}),
				'height':forms.NumberInput(attrs={'placeholder':'Height in cm','class':'form-control'}),
				'weight':forms.NumberInput(attrs={'placeholder':'Weight in Kg','class':'form-control'}),
				}
		labels={
				'name':'',
				'father_name':'',
				'mother_name':'',
				'spouse_name':'',
				'gender':'',
				'is_married':'',
				'dob':'Date of birth',
				'place_of_birth':'',
				'correspondence_address':'',
				'permanent_address':'',
				'pan':'',
				'aadhar':'',
				'education':'',
				'mobile':'',
				'height':'',
				'weight':'',
				'is_perm_same':'Same as correspondence address'
				}

	def clean_permanent_address(self):
		if self.cleaned_data['is_perm_same']:
			return self.cleaned_data['correspondence_address']
		else:
			return self.cleaned_data['permanent_address']

	
class PolicyForm(forms.ModelForm):
	class Meta:
		model=Policies
		fields='__all__'
		ordering = ['cid']
		labels={'cid':'Customer Id'}
		widgets={'cid':forms.TextInput(attrs={'readonly':'true'})}