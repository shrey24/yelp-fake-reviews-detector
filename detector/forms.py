from django import forms
from .models import ReviewInput

class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewInput
        fields = ('text',)
