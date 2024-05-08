from django import forms
from .models import *
from .models import Article


class AddForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [ 'title', 'content']




class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewModel
        fields = ['comment']




class ContactForm(forms.Form):
    name = forms.CharField(min_length=2,
                           widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-control w-100'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control w-100'}))


    message = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'placeholder': 'Message', 'cols': 30, 'rows': 9,
                                                                          'class': 'form-control w-100'}))



