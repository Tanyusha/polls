# coding=utf-8
from django.contrib.auth import login, authenticate

__author__ = 'Таника'
from django import forms as forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    # Return a 'disabled account' error message
                    pass
            else:
                # Return an 'invalid login' error message.
                pass

            return redirect('polls:poll_index')

    else:
        form = UserCreationForm()

    return render(request, "registration/registration.html",
                      {
                          'form': form,
                      })