# coding=utf-8
__author__ = 'Таника'

# coding=utf-8
from django import forms
from polls.models import Poll, Choice, ReceivePolls


class AddPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)
        widgets = {
            'question': forms.TextInput(attrs={'placeholder': 'poll'}),
        }

    # def __init__(self, user):
    #     super(AddPollForm, self).__init__(user)
    #     self.user = user


class AddChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
        widgets = {
            'choice_text': forms.TextInput(attrs={'placeholder': 'choice', 'autofocus':'autofocus'})
        }


class SendPollForm(forms.ModelForm):
    class Meta:
        model = ReceivePolls
        fields = ('user', )