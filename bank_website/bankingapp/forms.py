from django import forms
from .models import Person, Branch
class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'phoneno': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.Select(attrs={'class': 'form-control'}),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['area'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['area'].queryset = Branch.objects.filter(district_id=district_id).all()
            except (ValueError, TypeError):
                pass