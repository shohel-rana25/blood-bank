from django import forms
from .models import Bloodlist

class BloodlistInfomation(forms.ModelForm):
    class Meta:
        model=Bloodlist
        fields="__all__"
        labels={
            'Name':'Name', 
            'Last_Donate':'Last_Donate',
            'Location':'Location',
            'Phone':'Phone',
            'Email':'Email',
            'Blood_Group':'Blood_Group',
            'Image':'Image'
        }

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Last_Donate':forms.DateInput(attrs={'class':'form-control'}),
            'Location':forms.TextInput(attrs={'class':'form-control'}),
            'Phone':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Blood_Group':forms.Select(attrs={'class':'form-control'}),
            'Image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    
        }
