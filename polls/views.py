# coding=utf-8
# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from polls.forms import AddPollForm, AddChoiceForm, SendPollForm

from polls.models import Choice, Poll, ReceivePolls


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(user=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['recv_polls'] = ReceivePolls.objects.filter(user=self.request.user.pk)
        # print(list(ReceivePolls.objects.filter(user=self.request.user.pk)))
        return context


class DetailView(generic.DetailView):
    model = ReceivePolls
    template_name = 'polls/detail.html'
    pk_url_kwarg = 'recv_id'

    # def get_queryset(self):
    #     return ReceivePolls.objects.all()


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
    pk_url_kwarg = 'poll_id'


def add_poll(request):
    # return render(request, 'polls/add_poll.html')
    if request.method == "POST":
        form = AddPollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()
            return redirect('polls:add_choice', poll_id=poll.id)

    else:
        form = AddPollForm()  #request.user.username)

    poll = Poll.objects.all()

    return render(request, 'polls/add_poll.html',
                  {
                      'poll': poll,
                      'form': form,
                  })


def add_choice(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        form = AddChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.poll = poll
            choice.save()
            return redirect('polls:add_choice', poll_id=poll_id)

    else:
        form = AddChoiceForm()  #request.user.username)

    choices = poll.choice_set.all()

    return render(request, 'polls/add_choice.html', {
        'choices': choices,
        'form': form,
        'poll': poll,
    })


def vote(request, recv_id):
    recv_poll = get_object_or_404(ReceivePolls, pk=recv_id)
    try:
        selected_choice = recv_poll.poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'poll': recv_poll, 'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        recv_poll.is_answered = True
        recv_poll.answer = selected_choice.choice_text
        recv_poll.save()
        return redirect('polls:results', poll_id=recv_poll.poll.id)


def send(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == "POST":
        form = SendPollForm(request.POST)
        if form.is_valid():
            recv_polls = form.save(commit=False)
            recv_polls.poll = poll
            recv_polls.save()
            return redirect('polls:poll_index')

    else:
        form = SendPollForm()  #request.user.username)

    return render(request, 'polls/send.html', {
        'poll': poll,
        'form': form,
    })


def votes_details(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    selected_poll = ReceivePolls.objects.filter(poll_id=poll.id)
    print selected_poll
    choices = Choice.objects.filter(poll_id=poll.id)
    print choices
    for choice in choices:
        print choice.choice_text
    return render(request, 'polls/votes_details.html', {
        'poll': poll,
        'selected_poll': selected_poll,
        'choices': choices
    })


def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.user == poll.user:
        poll.delete()
    return redirect('polls:poll_index')


def edit(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = Choice.objects.filter(poll_id=poll.id)
    if request.method == "POST":
        k = request.POST.keys()
        for key in k:
            if key.startswith("choice_"):
                text, index = key.split('_', 1)
                choice = Choice.objects.get(id=index)
                if request.POST[key] == '':
                    choice.delete()
                else:
                    choice.choice_text = request.POST[key]
                    # print choice.choice_text
                    choice.save()
            else:
                if key.startswith("poll_question"):
                    if request.POST[key] == '':
                        poll.delete()
                        print "ddd"
                        return redirect('polls:del_message')
                    else:
                        poll.question = request.POST[key]
                        poll.save()
    return render(request, 'polls/edit.html', {
        'poll': poll,
        'choices': choices
    })


def choice_delete(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choice = get_object_or_404(Choice, id=choice_id)
    if request.user == poll.user:
        choice.delete()
    return redirect('polls:edit', poll_id=poll.id)


def del_message(request):
    return render(request, 'polls/del_message.html')