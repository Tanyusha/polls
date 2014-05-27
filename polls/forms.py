# coding=utf-8
__author__ = 'Таника'

# coding=utf-8
from django import forms
from polls.models import Poll, Choice


class AddPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question', 'user', 'pub_date')
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': 'poll'}),
        }

    # def __init__(self, user):
    #     super(AddPollForm, self).__init__(user)
    #     self.user = user


class AddChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('poll', 'choice_text', 'votes',)
        widgets = {
            'choice_text': forms.Textarea(attrs={'placeholder': 'choice'})
        }