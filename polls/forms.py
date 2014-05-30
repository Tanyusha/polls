# coding=utf-8
__author__ = 'Таника'

# coding=utf-8
from django import forms
from polls.models import Poll, Choice, ReceivePolls


class AddPollForm(forms.ModelForm):
    question = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Вопрос', 'autofocus':'autofocus'}), label='')
    class Meta:
        model = Poll
        fields = ('question',)


class AddChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Варианты ответов', 'autofocus':'autofocus'}), label='')
    class Meta:
        model = Choice
        fields = ('choice_text',)


class SendPollForm(forms.ModelForm):
    class Meta:
        model = ReceivePolls
        fields = ('user', )