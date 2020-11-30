from django import forms
from .models import Jobs


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['companyname', 'jobplace', 'jobprofile', 'experience', 'jobdescription','contact','email','applyHere']
        labels = {
            'companyname': 'Company Name', 'jobplace': 'Job Location', 'jobprofile': 'Job Profile', 'applyHere': 'Apply Here', 'jobdescription':'Job Description'
        }