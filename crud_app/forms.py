from django import forms
from crud_app.models import PersonData

class PersonDataForm(forms.ModelForm):
    class Meta:
        model = PersonData
        fields = '__all__'
        widgets = {
            "name" : forms.TextInput(attrs={"class":"form-control mt-2"}),
            "age" : forms.TextInput(attrs={"class":"form-control mt-2"}),
            "qualification" : forms.TextInput(attrs={"class":"form-control mt-2"}),
            "gender" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        }
