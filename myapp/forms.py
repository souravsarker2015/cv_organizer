from django import forms
from .models import CV

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Mymensingh', 'Mymensingh'),
    ('Barisal', 'Barisal'),
    ('Rangpur', 'Rangpur'),
    ('Comilla', 'Comilla'),
    ('Narayanganj', 'Narayanganj'),
    ('Gazipur', 'Gazipur'),
)


class CVForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefered Job Location', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = CV
        fields = ['name', 'date_of_birth', 'gender', 'locality', 'city', 'pin', 'state', 'phone', 'email', 'job_city', 'profile_image', 'profile_file']

        labels = {
            'name': 'Full Name',
            'date_of_birth': 'Date_of_Birth',
            'pin': 'Pin_code',
            'phone': 'Mobile No',
            'profile_image': 'Profile Image',
            'profile_file': 'Upload CV',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }
