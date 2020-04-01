from django import forms
from .models import Course


class CourseModelForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = [
      'title'
    ]
  
  # For validation
  # This work only on the form level does not do it on the model level
  def clean_title(self):
    title = self.cleaned_data.get('title')
    if title.lower() == 'abc' :
      raise forms.ValidationError('This is not a valid title')
    return title 
