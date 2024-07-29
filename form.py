from django import forms
from .models import Emp

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your Email ",max_length=100)
    name=forms.CharField(label="Enter your Name",max_length=100)
    feedback=forms.CharField(label="Your Feedback",widget=forms.Textarea)


    
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields=['name','emp_id','phone','address']