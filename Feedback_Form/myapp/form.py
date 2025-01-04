from django import forms
from myapp.models import Feedback_Form

class Feedback_Form1(forms.ModelForm):
    class Meta:
        model = Feedback_Form
        fields =['name','email','contact','feedback','rating']
